import unittest
from tool import language, benchmark, cmd

class BenchmarkTest(unittest.TestCase):

    def setUp(self, method):
        self.method = method
        self.cmd_by_langs = {}
        self.init()

    def init(self):
        for _lang in language.load_languages():
            _compile_cmd, _cmd = benchmark._get_benchmark_cmds(_lang, self.method)
            if _compile_cmd:
                # compile in advance
                _cp = cmd.run(_compile_cmd)
                if not _cp.returncode == 0:
                    raise RuntimeError(f"{_lang} compile failed: {_cp.stdout.decode('utf8')}")
            self.cmd_by_langs[_lang] = _cmd
