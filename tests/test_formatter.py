#!/usr/bin/env python3

from src.impsort.formatter import Formatter

FORMATTER = Formatter()


def test_simple(tmp_path):
    test_content = "import numpy as np\nimport matplotlib.pyplot as plt\nfrom os import path\nimport requests\nfrom delocate.fuse import wheels\nimport argparse\n\nif __name__ == '__main__':\n    print('bad juju')"
    target_content = "import argparse\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport requests\nfrom delocate.fuse import wheels\nfrom os import path\n\nif __name__ == '__main__':\n    print('bad juju')"
    p = tmp_path / "simple.py"
    p.write_text(test_content)
    assert p.read_text() == test_content
    FORMATTER.format_file(str(p))
    assert p.read_text() == target_content


def test_comments(tmp_path):
    test_content = "import numpy as np\nimport matplotlib.pyplot as plt\n# This has comments inside the import block\nfrom os import path\n#import requests\nfrom delocate.fuse import wheels\nimport argparse\n\nif __name__ == '__main__':\n    print('bad juju')"
    target_content = "import argparse\nimport matplotlib.pyplot as plt\n# This has comments inside the import block\nimport numpy as np\n#import requests\nfrom delocate.fuse import wheels\nfrom os import path\n\nif __name__ == '__main__':\n    print('bad juju')"
    p = tmp_path / "simple.py"
    p.write_text(test_content)
    assert p.read_text() == test_content
    FORMATTER.format_file(str(p))
    assert p.read_text() == target_content


def test_docstring(tmp_path):
    test_content = '"""This is an example of a file with a module docstring at the top\nrather than imports.\n"""\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom os import path\nimport requests\nfrom delocate.fuse import wheels\nimport argparse\n\nif __name__ == \'__main__\':\n    print(\'bad juju\')'
    target_content = '"""This is an example of a file with a module docstring at the top\nrather than imports.\n"""\nimport argparse\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport requests\nfrom delocate.fuse import wheels\nfrom os import path\n\nif __name__ == \'__main__\':\n    print(\'bad juju\')'
    p = tmp_path / "simple.py"
    p.write_text(test_content)
    assert p.read_text() == test_content
    FORMATTER.format_file(str(p))
    assert p.read_text() == target_content


def test_conditional(tmp_path):
    test_content = "import argparse\n\nif __name__ == '__main__':\n    test_conditional = True\n    if test_conditional:\n        import os\n        print('bad juju')"
    target_content = "import argparse\n\nif __name__ == '__main__':\n    test_conditional = True\n    if test_conditional:\n        import os\n        print('bad juju')"
    p = tmp_path / "conditional.py"
    p.write_text(test_content)
    assert p.read_text() == test_content
    FORMATTER.format_file(str(p))
    assert p.read_text() == target_content


def test_check_semantic(tmp_path):
    test_content = ""
    target_content = ""
    p = tmp_path / "check_semantic.py"
    p.write_text(test_content)
    assert p.read_text() == test_content
    FORMATTER.format_file(str(p), check_semantic=True)
    assert p.read_text() == target_content


# def test_grouping(tmp_path):
#     test_content = "import numpy as np\nfrom matplotlib import a, b, c, pyplot\n\nif __name__ == '__main__':\n    print('bad juju')"
#     target_content = "import numpy as np\nfrom matplotlib import(\n    a,\n    b,\n    c,\n    pyplot\n)\n\nif __name__ == '__main__':\n    print('bad juju')"
#     p = tmp_path / "simple.py"
#     p.write_text(test_content)
#     assert p.read_text() == test_content
#     FORMATTER.format_file(str(p))
#     assert p.read_text() == target_content
