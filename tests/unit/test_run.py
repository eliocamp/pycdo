from pycdo import cdo, cdo_cache, debug, geopotential
import os
from pathlib import Path
import tempfile
import shutil

if shutil.which("cdo") is None:
    os.environ["_DEBUG_SKIP_RUN"] = "true"

def test_no_cache():
    op = cdo(geopotential).ymonmean()

    cdo_cache.disable()
    # Execute normally
    out = op.execute()
    assert Path(out).is_file()
    os.unlink(out)

def test_cache():
    op = cdo(geopotential).ymonmean()

    cdo_cache.enable()
    # Without name 
    out1 = op.execute()
    assert Path(out1).is_file()

    out2 = op.execute()
    assert Path(out2).is_file()
    assert out1 == out2
    
    temp = tempfile.mktemp()
    op.execute(output = temp)
    assert Path(temp).is_file()    

    op.execute(output = temp)

def test_noop():
    assert cdo(geopotential).execute() == geopotential

def test_nooutput():
    debug.mockoutput.output = "\n# gridID 1"
    assert cdo(geopotential).griddes().execute()[1] == "# gridID 1"
    debug.mockoutput.output = None
    
    
