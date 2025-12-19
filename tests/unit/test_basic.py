from pycdo import cdo, cdo_options
import shlex

def expect_command(op, command):
    assert op._build() == command

def test_simple():
    """Builds a simple command with one file input"""
    expect_command(cdo("file.nc").ymonmean(), 
                   "cdo -ymonmean [ " + shlex.quote("file.nc") + " ]")


def test_two_files():
    """Builds a command with two inputs"""
    expect_command(cdo("file.nc").sub("file2.nc"),
                   "cdo -sub [ " + shlex.quote("file.nc") + " " + shlex.quote("file2.nc") + " ]")


def test_params():
    """Builds a command with parameters"""
    expect_command(cdo("file.nc").sellonlatbox(0, 360, -90, 0), 
                   "cdo -sellonlatbox,0,360,-90,0 [ " + shlex.quote("file.nc") + " ]")

def test_noinput():
    """Builds a command with no input file"""
    expect_command(cdo().topo("r360x180"), 
                   "cdo -topo,r360x180")

def test_nooutput():
    """Builds a command with no output"""
    expect_command(cdo("file.nc").griddes(), 
                   "cdo -griddes [ " + shlex.quote("file.nc") + " ]")

def test_chaining():
    """Chains commands"""
    expect_command(cdo("file.nc").sellonlatbox(0, 360, -90, 0).ymonmean(), 
                   "cdo -ymonmean [ -sellonlatbox,0,360,-90,0 [ " + shlex.quote("file.nc") + " ] ]")

def test_file_list():
    """Support for list of files as input"""
    expect_command(cdo(["file1", "file2"]).mergetime(), 
                   "cdo -mergetime [ file1 file2 ]")

    expect_command(cdo(["file1", "file2"]).mergetime(skip_same_time=True), 
                   "cdo -mergetime,True [ file1 file2 ]")

def test_options():
    cdo_options.set("-L")
    assert cdo_options.get() == "-L"

    expect_command(cdo("file"), "cdo -L file")

    assert cdo("file")._build(options = "-f nc") == "cdo -L -f nc file"
    assert cdo("file")._build(options = "-f nc", options_replace=True) == "cdo -f nc file"

    cdo_options.clear()
    assert cdo_options.get() == None


