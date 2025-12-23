

# Welcome to pycdo

|  |  |
|----|----|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/pycdo.svg)](https://pypi.org/project/pycdo/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/pycdo.svg)](https://pypi.org/project/pycdo/) |
| Coverage | [![Codecov test coverage](https://codecov.io/gh/eliocamp/pycdo/graph/badge.svg)](https://app.codecov.io/gh/eliocamp/pycdo) |
| Meta | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

pycdo is a wrapper for the Climate Data Operators (CDO). It allows
chaining CDO operators using method chaining and handles options and
temporary files for you.

## Get started

You can install this package into your preferred Python environment
using pip:

``` bash
pip install pycdo
```

## Example

``` python
from pycdo import cdo, cdo_options, cdo_cache, geopotential
```

The ymonmean operator computes monthly annual cycle. The pycdo function
is `cdo_ymonmean()`

``` python
cdo(geopotential).ymonmean()
```

    CDO operation.
    cdo -Z -ymonmean [ /home/user1/Documents/python/pycdo/src/pycdo/data/geopotential.nc ] {output}

The output just prints the command with a place holder output. Use
`.execute()` to actually run the command. If no output file is
specified, then the result is saved in a tempfile.

``` python
cdo(geopotential).ymonmean().execute()
```

    'data/pycdo/0c0a0266756e38030d8b79951f43651f'

Operators can be chained. Lets select just the Southern Hemisphere
first.

``` python
(
    cdo(geopotential)
    .sellonlatbox(0, 360, -90, 0)
    .ymonmean()
    .execute()
)
```

    'data/pycdo/e84e35ae09335bdd4c8fa3585279b722'

We can save operations to execute later or as input for other operations

``` python
sh_geopotential = (
    cdo(geopotential)
    .sellonlatbox(0, 360, -90, 0)
    .sellevel(300)
    .ymonmean()
) 

cdo(sh_geopotential).ymonmean().execute()
```

    'data/pycdo/fe3e3dbfe5ee9d93c21b9824c81173ba'

Temporary files are deleted when the variables holding them are garbage
collected to prevent blowing up disk space when iterating over the same
code.

For long-running operations, you can set up a cache.

``` python
cdo_cache.set("data/pycdo")
```

    <pycdo.cdo_cache.CdoCache at 0x79ad1c6dae10>

This turns off the automatic deletion and returns existing files instead
of re-runing CDO operators.

``` python
import time
# First run. 
start = time.time()
sh_geopotential.execute()
time.time() - start
```

    0.06971979141235352

``` python
# Second run just returns the existing file
start = time.time()
sh_geopotential.execute()
time.time() - start
```

    0.0008301734924316406

You can set global options that will apply to all operations.

``` python
cdo_options.set("-Z")  # Compress result
sh_geopotential
```

    CDO operation.
    cdo -Z -ymonmean [ -sellevel,300 [ -sellonlatbox,0,360,-90,0 [ /home/user1/Documents/python/pycdo/src/pycdo/data/geopotential.nc ] ] ] {output}

## Copyright

- Copyright © 2025 Elio Campitelli.
- Free software distributed under the [MIT License](./LICENSE).
