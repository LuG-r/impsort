# impsort
The Python utility to organise your imports!

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---
impsort will organise your imports alphabetically, grouping by  `import` first and then `from` second. 


<table>
<tr>
<th>Original</th>
<th>impsort</th>
</tr>
<tr>
<td>

```python
import numpy as np
import matplotlib.pyplot as plt
from os import path
import requests
from delocate.fuse import wheels
import argparse
```

</td>
<td>

```python
import argparse
import matplotlib.pyplot as plt
import numpy as np
import requests
from delocate.fuse import wheels
from os import path
```

<td>
</tr>
</table>



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