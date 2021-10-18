import unittest
from tool import cmd
from test.benchmark.benchmark_test import BenchmarkTest

class FizzBuzzIncrementTest(BenchmarkTest):

    def setUp(self):
        super().setUp('increment')

    def test_15(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['15']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('fizzbuzz:1', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz:4', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz:2', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('none:8', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_30(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['30']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('fizzbuzz:2', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz:8', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz:4', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('none:16', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_100(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['100']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('fizzbuzz:6', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz:27', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz:14', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('none:53', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_1000(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['1000']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('fizzbuzz:66', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz:267', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz:134', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('none:533', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

if __name__ == "__main__":
    unittest.main()
