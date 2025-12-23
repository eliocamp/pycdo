

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
    cdo -ymonmean [ /home/user1/Documents/python/pycdo/src/pycdo/data/geopotential.nc ] {output}

The output just prints the command with a place holder output. Use
`.execute()` to actually run the command. If no output file is
specified, then the result is saved in a tempfile.

``` python
cdo(geopotential).ymonmean().execute()
```

    '/tmp/tmp_v6j9iii'

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

    '/tmp/tmphgu_ynz8'

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

    '/tmp/tmprz881j79'

Temporary files are deleted when the variables holding them are garbage
collected to prevent blowing up disk space when iterating over the same
code.

For long-running operations, you can set up a cache.

``` python
cdo_cache.set("data/pycdo")
```

    <pycdo.cdo_cache.CdoCache at 0x7fe94ea83da0>

This turns off the automatic deletion and returns existing files instead
of re-runing CDO operators.

``` python
import time
start = time.time()
sh_geopotential.execute()
time.time() - start
```

    0.05309128761291504

The second run just returns the existing file, so it’s faster.

``` python
start = time.time()
sh_geopotential.execute()
time.time() - start
```

    0.0008449554443359375

``` python
cdo_cache.forget() # Cleanup cache
```

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
