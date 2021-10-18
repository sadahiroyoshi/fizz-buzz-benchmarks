import subprocess
from tool import cmd

def load_languages():
    """
    load all languages in conf/languages.csv.

    Returns
    -------
    langs : list
        languages in conf/languages.csv.
    """
    _langs = []
    with open('conf/languages.csv') as f:
        for _line in f.readlines():
            _langs.append(_line[0:-1]) # chop line separetor
    return _langs

def print_version(lang):
    """
    print the version of language on your device.

    Parameters
    -------
    lang : str
        the language which is wanted to print a version.
    """
    _cmd = _get_cmd_of_version(lang)
    _cp = cmd.run(_cmd)
    if not _cp.returncode == 0:
        raise TypeError(f"Failed to Print {lang} Version: {_cp.stdout.decode('utf8')}")
    print(f"{lang}:\n{_cp.stdout.decode('utf8')}")

def _get_cmd_of_version(lang):
    if (lang == 'python'):
        return ['python', '--version']
    elif (lang == 'rust'):
        return ['rustc', '--version']
    elif (lang == 'go'):
        return ['go', 'version']
    elif (lang == 'scala'):
        return ['scala', '--version']
    elif (lang == 'c'):
        return ['cc', '--version']
    elif (lang == 'java'):
        return ['java', '--version']
    elif (lang == 'ruby'):
        return ['ruby', '--version']
    elif (lang == 'dart'):
        return ['dart', '--version']
    # not programing language but engine. 
    elif (lang == 'nodejs'):
        return ['node', '--version']
    else:
        raise TypeError(f"Not Supported: {lang}")
