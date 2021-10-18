import timeit
import subprocess

# used in calc()
_setup_str = f"""
import subprocess
def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
"""

def run(cmd):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def calculate(cmd, number=1, repeat=100):
    return timeit.repeat(stmt=f"run({cmd})", setup=_setup_str, number=number, repeat=repeat)
