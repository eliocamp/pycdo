import pytest
import tempfile
from pathlib import Path

from pycdo.cdo_cache import CdoCache


class TestCdoCacheInit:
    """Test CdoCache initialization"""
    
    def test_init_defaults(self):
        """Test initialization with default values"""
        cache = CdoCache()
        assert cache.path is None
        assert cache.enabled is False
        assert cache.old is None
    
    def test_init_with_values(self):
        """Test initialization with custom values"""
        cache = CdoCache(path="/tmp/cache", enabled=True)
        assert cache.path == "/tmp/cache"
        assert cache.enabled is True
        assert cache.old is None

    def test_cannot_enable_with_none(self):
        with pytest.raises(ValueError): 
            cache = CdoCache(path=None, enabled=True)
    

class TestCdoCacheClone:
    """Test _clone method"""
    
    def test_clone_creates_independent_copy(self):
        """Test that clone creates an independent copy"""
        cache1 = CdoCache(path="/tmp/cache1", enabled=True)
        cache2 = cache1._clone()
        
        assert cache2.path == cache1.path
        assert cache2.enabled == cache1.enabled
        assert cache2.old == cache1.old
        
        # Verify they are independent
        cache2.path = "/tmp/cache2"
        assert cache1.path == "/tmp/cache1"


class TestCdoCacheSet:
    """Test set method"""
    
    def test_set_path(self):
        """Test setting a new cache path"""
        cache = CdoCache()
        old = cache.set("/tmp/new_cache")
        
        assert cache.path == "/tmp/new_cache"
        assert cache.enabled is True
        assert isinstance(old, CdoCache)
        assert old.path is None
        assert old.enabled is False
    
    def test_set_enables_cache(self):
        """Test that set always enables caching"""
        cache = CdoCache(path="/tmp/cache", enabled=False)
        cache.set("/tmp/new_cache")
        
        assert cache.enabled is True
    
    def test_set_with_cache_instance(self):
        """Test setting with a CdoCache instance"""
        cache1 = CdoCache(path="/tmp/cache1", enabled=True)
        cache2 = CdoCache(path="/tmp/cache2", enabled=False)
        
        old = cache2.set(cache1)
        
        assert cache2.path == "/tmp/cache1"
        assert cache2.enabled is True
    
    def test_set_saves_old_state(self):
        """Test that set saves the old state"""
        cache = CdoCache(path="/tmp/original", enabled=True)
        old = cache.set("/tmp/new")
        
        assert cache.old is old
        assert cache.old.path == "/tmp/original"

    def test_cannot_set_none(self):
        cache = CdoCache(path="/tmp/original", enabled=True)
        with pytest.raises(ValueError):
            cache.set(path = None)

class TestCdoCacheRestore:
    """Test restore method"""
    
    def test_restore_to_previous_state(self):
        """Test restoring to previous state"""
        cache = CdoCache(path="/tmp/original", enabled=True)
        cache.set("/tmp/new")
        cache.restore()
        
        assert cache.path == "/tmp/original"
        assert cache.enabled is True

        cache.disable()
        cache.restore()
        assert cache.enabled is True
    
    def test_restore_without_old_state_raises_error(self):
        """Test that restore raises error when no old state exists"""
        cache = CdoCache()
        
        with pytest.raises(ValueError, match="Cannot restore cache"):
            cache.restore()
    
    def test_restore_multiple_times(self):
        """Test multiple restore operations"""
        cache = CdoCache(path="/tmp/state1", enabled=True)
        
        cache.set("/tmp/state2")
        cache.set("/tmp/state3")
        
        cache.restore()
        cache.restore()
        assert cache.path == "/tmp/state1"


class TestCdoCacheDisable:
    """Test disable method"""
    
    def test_disable_turns_off_caching(self):
        """Test that disable turns off caching"""
        cache = CdoCache(path="/tmp/cache", enabled=True)
        cache.disable()
        
        assert cache.enabled is False
        assert cache.path == "/tmp/cache"
        
    
    def test_disable_saves_old_state(self):
        """Test that disable saves the old state"""
        cache = CdoCache(path="/tmp/cache", enabled=True)
        old = cache.disable()
        
        assert isinstance(old, CdoCache)
        assert cache.old is old
        assert cache.old.enabled is True


class TestCdoCacheEnable:
    """Test enable method"""
    
    def test_enable_turns_on_caching(self):
        """Test that enable turns on caching"""
        cache = CdoCache(path="/tmp/cache", enabled=False)
        cache.enable()
        
        assert cache.enabled is True
        assert cache.is_enabled() is True
        assert cache.path == "/tmp/cache"
        
    
    def test_enable_saves_old_state(self):
        """Test that enable saves the old state"""
        cache = CdoCache(path="/tmp/cache", enabled=False)
        old = cache.enable()
        
        assert isinstance(old, CdoCache)
        assert cache.old is old
        assert cache.old.is_enabled() is False


class TestCdoCacheForget:
    """Test forget method"""
    
    def test_forget_removes_all_files(self):
        """Test that forget removes all files from cache directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = CdoCache(path=tmpdir, enabled=True)
            
            # Create some test files
            Path(tmpdir, "file1.txt").write_text("test1")
            Path(tmpdir, "file2.txt").write_text("test2")
            
            # Create subdirectories with files
            subdir = Path(tmpdir, "subdir")
            subdir.mkdir()
            (subdir / "file3.txt").write_text("test3")
            
            # Verify files exist
            assert len(list(Path(tmpdir).rglob("*"))) > 0
            
            # Forget should remove all files but keep directory
            cache.forget()
            
            assert Path(tmpdir).exists()
            assert Path(tmpdir).is_dir()
            assert len(list(Path(tmpdir).glob("*"))) == 0
    

