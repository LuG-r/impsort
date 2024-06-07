# impsort
The Python utility to organise your imports!

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---
impsort will organise your imports alphabetically, grouping by  `import` first and then `from` second. 


```python
# Not sorted at all
import numpy as np
import matplotlib.pyplot as plt
from os import path
import requests
from delocate.fuse import wheels
import argparse
```

```python
# Sorted with impsort
import argparse
import matplotlib.pyplot as plt
import numpy as np
import requests
from delocate.fuse import wheels
from os import path
```

impsort will organise the imports but will not move other code around. Commented out lines, including docstrings, will be ignored as will conditional imports.

```python
"""
This is an example of a file with a module docstring at the top rather than imports.
"""
import numpy as np
import matplotlib.pyplot as plt
from os import path
#import requests
from delocate.fuse import wheels
import argparse


if test_condition:
    import os
```

```python
"""
This is an example of a file with a module docstring at the top rather than imports.
"""
import argparse
import matplotlib.pyplot as plt
import numpy as np
#import requests
from delocate.fuse import wheels
from os import path


if test_condition:
    import os
```



## Installation
```shell
# clone the repository
git clone git@github.com:LuG-r/impsort.git
```

## Usage
Currently, impsort can only be used against single files. Support for directory level usage is coming soon!
```shell
# run the formatter
python impsort/src/main.py path/to/file.py
```