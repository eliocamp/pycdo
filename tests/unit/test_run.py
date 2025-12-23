from pycdo import cdo, cdo_cache
import os
from pathlib import Path
import tempfile
import shutil

if shutil.which("cdo") is None:
    os.environ["_DEBUG_SKIP_RUN"] = "true"


def test_no_cache():
    test_file = str(Path(__file__).parent.parent / "data" / "test.nc")
    op = cdo(test_file).ymonmean()

    cdo_cache.disable()
    # Execute normally
    out = op.execute()
    assert Path(out).is_file()
    os.unlink(out)

def test_cache():
    test_file = str(Path(__file__).parent.parent / "data" / "test.nc")
    op = cdo(test_file).ymonmean()

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
    test_file = str(Path(__file__).parent.parent / "data" / "test.nc")
    assert cdo(test_file).execute() == test_file

def test_nooutput():
    test_file = str(Path(__file__).parent.parent / "data" / "test.nc")
    assert cdo(test_file).griddes().execute()[1] == "# gridID 1"
    
    
