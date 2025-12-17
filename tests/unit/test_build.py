import pytest
from pycdo import cdo

def test_ymonmean_build():
    op = cdo("file.nc").ymonmean()
    assert op._build() == "cdo -ymonmean file.nc"
