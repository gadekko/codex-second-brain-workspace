import copy
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error
import jev_decide as j

EXAMPLES = Path(__file__).resolve().parents[1] / 'examples'


class JevTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name)/'cache.sqlite3'
        self.config = json.loads((EXAMPLES/'jev-config.json').read_text())
        self.config.update(enabled=True, mode='assist', evaluation_id='synthetic-test')
        self.request = json.loads((EXAMPLES/'jev-request.json').read_text())
        self.calls = 0
        self.env = patch.dict(os.environ, {'TYPESAFE_API_KEY': 'synthetic-test-key'})
        self.env.start()
        self.addCleanup(self.env.stop)

    def response(self, body, key):
        self.calls += 1
        answers = {}
        for name, q in body['questions'].items():
            labels = list(q['criteria'])
            answers[name] = {'type': 'choice', 'choice': labels[0], 'confidence': 0.97,
                             'probabilities': {k: 1.0 if k == labels[0] else 0.0 for k in labels}}
        return {'model': body['model'], 'answers': answers,
                'usage': {'input_tokens': 500, 'output_tokens': 20}}

    def run_decision(self, **kwargs):
        return j.decide(self.config, self.request, self.db, live=True, send=self.response, **kwargs)

    def test_disabled_dry_run_and_missing_key_never_connect(self):
        self.config['enabled'] = False
        self.assertEqual(self.run_decision()['reason'], 'disabled')
        self.config['enabled'] = True
        self.assertEqual(j.decide(self.config, self.request, self.db)['reason'], 'dry_run')
        with patch.dict(os.environ, {'TYPESAFE_API_KEY': ''}):
            self.assertEqual(self.run_decision()['reason'], 'missing_api_key')
        self.assertEqual(self.calls, 0)
        self.assertFalse(self.db.exists())

    def test_workflow_recommendation_never_authorizes_execution(self):
        result = self.run_decision()
        self.assertEqual(result['recommendations'], {'route': 'meeting_prep'})
        self.assertFalse(result['external_actions_authorized'])
        self.assertEqual(result['route'], 'existing_codex_workflow')
        self.assertAlmostEqual(result['estimated_usd_this_run'], 0.000021)

    def test_shadow_observes_without_routing(self):
        self.config['mode'] = 'shadow'
        result = self.run_decision()
        self.assertEqual(result['status'], 'shadow')
        self.assertEqual(result['recommendations'], {})
        self.assertTrue(result['observed_answers'])

    def test_batch_relevance_in_single_call(self):
        self.request['kind'] = 'relevance'
        result = self.run_decision()
        self.assertEqual(len(result['recommendations']), 2)
        self.assertEqual(self.calls, 1)

    def test_cache_respects_source_and_expiry(self):
        self.assertFalse(self.run_decision(now=10000)['cache_hit'])
        cached = self.run_decision(now=10001)
        self.assertTrue(cached['cache_hit'])
        self.assertEqual(cached['estimated_usd_this_run'], 0)
        self.request['source_version'] = 'changed'
        self.assertFalse(self.run_decision(now=10002)['cache_hit'])
        self.assertFalse(self.run_decision(now=15000)['cache_hit'])
        self.assertEqual(self.calls, 3)
        raw = self.db.read_bytes()
        self.assertNotIn(self.request['context'].encode(), raw)
        self.assertNotIn(b'synthetic-test-key', raw)

    def test_budgets_block_new_calls_but_allow_cache(self):
        self.config['max_daily_calls'] = 1
        self.run_decision(now=10000)
        self.assertTrue(self.run_decision(now=10001)['cache_hit'])
        self.request['source_version'] = 'new'
        self.assertEqual(self.run_decision(now=10002)['reason'], 'daily_budget')
        self.config['max_daily_calls'] = 100
        self.config['max_daily_usd'] = 0.000001
        self.assertEqual(self.run_decision(now=10003)['reason'], 'daily_budget')
        self.assertEqual(self.calls, 1)

    def test_low_confidence_none_and_uncertain_fall_back(self):
        original = self.response
        def low(body, key):
            response = original(body, key)
            response['answers']['route']['confidence'] = 0.1
            return response
        result = j.decide(self.config, self.request, self.db, live=True, send=low)
        self.assertEqual(result['recommendations'], {})
        self.assertEqual(result['status'], 'fallback')
        for kind, label in [('workflow', 'none'), ('relevance', 'uncertain')]:
            def abstain(body, key):
                response = original(body, key)
                for answer in response['answers'].values():
                    answer['choice'] = label
                    answer['probabilities'] = {k: float(k == label) for k in answer['probabilities']}
                return response
            self.request['kind'] = kind
            self.request['source_version'] = label
            self.assertEqual(j.decide(self.config, self.request, self.db, live=True,
                                      send=abstain)['recommendations'], {})

    def test_malformed_responses_rejected(self):
        body = j.build_request(self.request, self.config['model'])
        good = self.response(body, 'test')
        changes = [lambda r: r.update(model='jev-latest'),
                   lambda r: r.update(answers={}),
                   lambda r: r['answers']['route'].update(choice='send_email'),
                   lambda r: r['answers']['route'].update(confidence=float('nan')),
                   lambda r: r['answers']['route'].update(probabilities={'meeting_prep': 1}),
                   lambda r: r['answers']['route']['probabilities'].update(none=-1),
                   lambda r: r['usage'].update(input_tokens=True)]
        for mutate in changes:
            bad = copy.deepcopy(good)
            mutate(bad)
            with self.assertRaises(ValueError):
                j.validate_response(bad, body)

    def test_network_failures_are_redacted_and_not_retried(self):
        calls = []
        def fail(body, key):
            calls.append(1)
            raise urllib.error.HTTPError(j.ENDPOINT, 429, 'SECRET REQUEST CONTENT', {}, None)
        result = j.decide(self.config, self.request, self.db, live=True, send=fail)
        self.assertEqual(result['reason'], 'connection_or_response_failure')
        self.assertNotIn('SECRET', json.dumps(result))
        self.assertEqual(len(calls), 1)

    def test_redirects_are_refused(self):
        with self.assertRaises(ValueError):
            j.NoRedirect().redirect_request(None, None, 302, '', {}, 'https://example.org')

    def test_oversize_invalid_and_unevaluated_requests_never_connect(self):
        self.request['context'] = 'x' * 25000
        self.assertEqual(self.run_decision()['reason'], 'invalid_local_input')
        self.request['context'] = 'Reply'
        self.config['evaluation_id'] = None
        self.assertEqual(self.run_decision()['reason'], 'invalid_local_input')
        self.config['evaluation_id'] = 'test'
        self.config['model'] = 'jev-latest'
        self.assertEqual(self.run_decision()['reason'], 'invalid_local_input')
        self.assertEqual(self.calls, 0)

    def test_transport_uses_official_contract(self):
        body = j.build_request(self.request, self.config['model'])
        expected = self.response(body, 'test')
        with patch.object(j.urllib.request, 'build_opener') as opener:
            response = opener.return_value.open.return_value.__enter__.return_value
            response.read.return_value = json.dumps(expected).encode()
            self.assertEqual(j.transport(body, 'synthetic-key'), expected)
            args, kwargs = opener.return_value.open.call_args
            request = args[0]
            self.assertEqual(request.full_url, j.ENDPOINT)
            self.assertEqual(request.method, 'POST')
            self.assertEqual(json.loads(request.data), body)
            self.assertEqual(request.get_header('Authorization'), 'Bearer synthetic-key')
            self.assertEqual(kwargs['timeout'], 15)
            self.assertIs(opener.call_args.args[0], j.NoRedirect)

    def test_probability_gate_and_changed_context(self):
        def uncertain(body, key):
            response = self.response(body, key)
            response['answers']['route']['probabilities'] = {
                'meeting_prep': 0.6, 'reply_draft': 0.4, 'none': 0.0}
            return response
        result = j.decide(self.config, self.request, self.db, live=True, send=uncertain)
        self.assertEqual(result['status'], 'fallback')
        self.request['context'] = 'Prepare a brief for an upcoming meeting.'
        self.assertFalse(self.run_decision()['cache_hit'])
        self.assertEqual(self.calls, 2)

    def test_threshold_change_rechecks_cached_result(self):
        self.run_decision()
        self.config['min_confidence'] = 0.99
        result = self.run_decision()
        self.assertTrue(result['cache_hit'])
        self.assertEqual(result['status'], 'fallback')


if __name__ == '__main__':
    unittest.main()
