import unittest
from tool import cmd
from test.benchmark.benchmark_test import BenchmarkTest

class FizzBuzzPrintlnTest(BenchmarkTest):

    def setUp(self):
        super().setUp('println')

    def test_1(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['1']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('1', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('fizz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('buzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('fizzbuzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_3(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['3']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('2', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('buzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('fizzbuzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_5(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['5']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('4', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('fizzbuzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_10(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['10']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('8', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertNotIn('fizzbuzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

    def test_15(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _args = ['15']
            _cp = cmd.run(_cmd + _args)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")
            self.assertIn('14', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('buzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")
            self.assertIn('fizzbuzz', _cp.stdout.decode('utf8'), f"{_lang}:{self.method} invalid logic")

if __name__ == "__main__":
    unittest.main()
