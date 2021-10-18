import unittest
from tool import cmd
from test.benchmark.benchmark_test import BenchmarkTest

class FizzBuzzNothingTest(BenchmarkTest):

    def setUp(self):
        super().setUp('nothing')

    def test_success(self):
        for _lang, _cmd in self.cmd_by_langs.items():
            _cp = cmd.run(_cmd)
            self.assertEqual(0, _cp.returncode, f"{_lang}:{self.method} failed")

if __name__ == "__main__":
    unittest.main()
