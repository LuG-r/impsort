import os
import subprocess

ENTRY_POINT = "/Users/lucasg/dev/impsort/src/main.py"

def test_cli_help():
    exit_status = os.system(f"python3 {ENTRY_POINT} -h")
    assert exit_status == 0


def test_cli_non_py_input():
    result = subprocess.check_output(
        [f"python3 {ENTRY_POINT} requirements.txt"], 
        shell=True, 
        stderr=subprocess.STDOUT, 
        text=True
    )
    assert result == "The file provided does not appear to be a Python file\n"