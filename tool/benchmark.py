import os
import string
from tool import cmd

def calc_benchmark(method, lang, n, r):
    """
    calculate the benchmark of the method of the language.

    Parameters
    -------
    method : str
        the method of the calclations of benchmarks.
    lang : str
        the language which is wanted to calculate a benchmark.
    n : int
        the number of the calclations of benchmarks.
    r : int
        the number of repeat. It will be the number of each result lists.

    Returns
    -------
    results : list
        the repeated benchmark results of the method of the language.
    """
    _compile_cmd, _cmd = _get_benchmark_cmds(lang, method)
    print(f"{lang} running...")

    # run compile in advance
    if _compile_cmd:
        print(f"compile:{_compile_cmd}")
        cmd.run(_compile_cmd)

    # run cmd
    _args = [str(n)]
    print(f"run:{_cmd + _args}")
    # `number=1` as the method of each langs are called {n} times in each scripts
    # `repeat=(r + 1)` as the first run will be ignored
    _results = cmd.calculate((_cmd + _args), number=1, repeat=(r + 1))

    print("ignore the first run as noise removing")
    _results.pop(0)

    print(f"{lang} finished...")
    return _results

def _get_benchmark_cmds(lang, method):
    """
    get cmds for benchmarks.

    Returns
    -------
    compile_cmd : list
        cmd to compile.
    cmd : list
        cmd to run.
    """
    _base_script_dir = _build_base_script_dir(lang)
    if not os.path.exists(_base_script_dir):
        raise TypeError(f"No {lang} Script Directory: {_base_script_dir}")
    _script_dir = _build_script_dir(lang, method)
    if not os.path.exists(_script_dir):
        raise TypeError(f"No {lang}:{method} Script Directory: {_script_dir}")

    if (lang == 'python'):
        return (
            [],
            ['python', f"{_script_dir}/fizz_buzz_{method}.py"],
        )
    elif (lang == 'rust'):
        return (
            ['cargo', 'build', '--release', '--manifest-path', f"{_script_dir}/Cargo.toml"],
            [f"{_script_dir}/target/release/fizz_buzz_{method}"],
        )
    elif (lang == 'go'):
        return (
            ['go', 'build', '-o', f"{_script_dir}/target/", f"{_script_dir}/fizz_buzz_{method}.go"],
            [f"{_script_dir}/target/fizz_buzz_{method}"],
        )
    elif (lang == 'scala'):
        return (
            ['scalac', '-d', f"{_script_dir}/target/", f"{_script_dir}/FizzBuzz{_snake_to_pascal(method)}.scala"],
            ['scala', '-cp', f"{_script_dir}/target", f"FizzBuzz{_snake_to_pascal(method)}"],
        )
    elif (lang == 'c'):
        return (
            ['cc', f"{_script_dir}/fizz_buzz_{method}.c", '-o', f"{_script_dir}/target/fizz_buzz_{method}"],
            [f"{_script_dir}/target/fizz_buzz_{method}"],
        )
    elif (lang == 'java'):
        return (
            ['javac', '-d', f"{_script_dir}/target/", f"{_script_dir}/FizzBuzz{_snake_to_pascal(method)}.java"],
            ['java', '-cp', f"{_script_dir}/target", f"FizzBuzz{_snake_to_pascal(method)}"],
        )
    elif (lang == 'ruby'):
        return (
            [],
            ['ruby', f"{_script_dir}/fizz_buzz_{method}.rb"],
        )
    elif (lang == 'dart'):
        return (
            ['dart', 'compile', 'exe', f"{_script_dir}/fizz_buzz_{method}.dart", '-o', f"{_script_dir}/target/fizz_buzz_{method}"],
            [f"{_script_dir}/target/fizz_buzz_{method}"],
        )
    # not programing language but engine. 
    elif (lang == 'nodejs'):
        return (
            [],
            ['node', f"{_script_dir}/fizz_buzz_{method}_compiled.js"], # manually compiled
        )
    else:
        raise TypeError(f"Not Supported: {lang}")

def _build_base_script_dir(lang) -> str:
    return f"{os.getcwd()}/script/{lang}"

def _build_script_dir(lang, method) -> str:
    return f"{_build_base_script_dir(lang)}/{method}"

def _snake_to_pascal(str) -> str:
    return string.capwords(str.replace("_", " ")).replace(" ", "")
