import sys
import os

if __name__ == '__main__':
    dir = os.path.dirname(sys.argv[0])
    test_contents = {
        'simple': "import numpy as np\nimport matplotlib.pyplot as plt\nfrom os import path\nimport requests\nfrom delocate.fuse import wheels\nimport argparse\n\nif __name__ == '__main__':\n    print('bad juju')",
        'docstring': "\"\"\"This is an example of a file with a module docstring at the top\nrather than imports.\n\"\"\"\nimport numpy as np\nimport matplotlib.pyplot as plt\nfrom os import path\nimport requests\nfrom delocate.fuse import wheels\nimport argparse\n\nif __name__ == '__main__':\n    print('bad juju')",
        'comments': "import numpy as np\nimport matplotlib.pyplot as plt\n# This has comments inside the import block\nfrom os import path\n#import requests\nfrom delocate.fuse import wheels\nimport argparse\n\nif __name__ == '__main__':\n    print('bad juju')"
    }

    for test in test_contents:
        with open(f"{dir}/../tests/{test}.py", "w") as f:
            f.write(test_contents[test])