import gc
import os
import tempfile
from pathlib import Path
from pycdo.ephemeral_file import EphemeralFile


def make_file(content=None):
    """Create a temporary file in a temporary directory.
    
    Parameters
    ----------
    content : str, optional
        If provided, write this content to the file.
    
    Returns
    -------
    tuple
        (path, temp_dir) where path is the file path and temp_dir is the parent directory.
    """
    temp_dir = tempfile.mkdtemp()
    fd, path = tempfile.mkstemp(dir=temp_dir)
    os.close(fd)
    return path, temp_dir


def cleanup(path, temp_dir):
    """Clean up a file and directory if they exist."""
    if Path(path).exists():
        os.remove(path)
    if Path(temp_dir).exists():
        os.rmdir(temp_dir)
    

def test_ephemeral_file_is_string():
    """EphemeralFile should be a string subclass."""
    path, temp_dir = make_file()
    
    ef = EphemeralFile(path)
    assert isinstance(ef, str)
    assert ef == path
    
    cleanup(path, temp_dir)

def test_file_deleted_on_garbage_collection():
    """File should be deleted when EphemeralFile is garbage collected."""
    path, _ = make_file("test content")
    assert Path(path).exists()
    
    # Create EphemeralFile and delete it
    ef = EphemeralFile(path)
    del ef
    gc.collect()
    
    # File should be deleted
    assert not Path(path).exists()

def test_temp_directory_deleted_when_empty():
    """Temporary directory should be deleted when it becomes empty."""
    path, temp_dir = make_file("test content")
    
    # Create EphemeralFile and delete it
    ef = EphemeralFile(path)
    del ef
    gc.collect()

    assert not Path(temp_dir).exists()

def test_temp_directory_not_deleted_if_not_empty():
    """Temporary directory should not be deleted if it contains other files."""
    temp_dir = tempfile.mkdtemp()
    _, path1 = tempfile.mkstemp(dir=temp_dir)
    _, path2 = tempfile.mkstemp(dir=temp_dir)
    
    # Delete first EphemeralFile
    ef1 = EphemeralFile(path1)
    del ef1
    gc.collect()
    
    # Directory should still exist because path2 is still there
    assert not Path(path1).exists()
    assert Path(temp_dir).exists()
    assert Path(path2).exists()
    
    os.remove(path2)
    os.rmdir(temp_dir)

def test_nonexistent_file_not_error():
    """Deleting EphemeralFile with nonexistent file should not raise error."""
    path, temp_dir = make_file()
    
    # Don't create the file (just use the path)
    ef = EphemeralFile(path)
    
    os.remove(path)
    # Should not raise an error
    del ef
    gc.collect()
 
    assert not Path(path).exists()
    assert not Path(temp_dir).exists()

def test_ephemeral_file_usable_with_open():
    """EphemeralFile should be usable with open() function."""
    path, temp_dir = make_file()
    
    ef = EphemeralFile(path)
    
    # Should be able to use as file path
    with open(ef, 'w') as f:
        f.write("test data")
    
    # f holds a reference to ef it needs to be deleted
    del f
    gc.collect()   

    assert Path(path).exists()

    # Cleanup
    del ef
    gc.collect()
    
    
    assert not Path(path).exists()
    assert not Path(temp_dir).exists()

def test_list_ephemeral_files():
    paths = [path for path, _ in (make_file() for n in range(2))]
    assert all([Path(path).exists() for path in paths])

    efs = [EphemeralFile(x) for x in paths]

    f = efs[0]

    del efs
    gc.collect()

    assert Path(paths[0]).exists()
    assert not Path(paths[1]).exists()
