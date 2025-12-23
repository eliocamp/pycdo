import shutil
import os
import tempfile
from pathlib import Path

class CdoCache:
    """
    Cache management 

    The cdo_cache module provides a global cache object for managing CDO operation results.
    By default, CDO operations create temporary files that are deleted after use. The cache 
    allows you to persist these results to disk for faster re-execution of the same operations.

    The cdo_cache is a global CdoCache instance that manages a persistent cache directory.
    Users interact with cdo_cache directly rather than instantiating CdoCache themselves.

    
    """
    def __init__(self, path = None, enabled = False, old = None):
        self._validate_path(path, enabled)
        self.path = path
        self.enabled = enabled
        self.old = old

    def _clone(self):
        return CdoCache(path = self.path, enabled = self.enabled, old = self.old)

    def _validate_path(self, path, enabled):
        if path is None and enabled:
            raise ValueError("Cannot enable cache with path None")

    def set(self, path):
        """
        Define the path of the cache. 

        Parameters
        ---------
        path : str, None or CdoCache 
            Path to the cache. If it's None, then a temporary 
            directory will be used. Can also accept a CdoCache 
            object to enable the idiom
            `
            old = cdo_cache.set(path)
            cdo_cache.set(old)
            `
        
        Returns
        -------
        A CdoCache object with the previous state. 
        """
        self._validate_path(path, True)
        # Create a new instance to return 
        old = self._clone()
        enabled = True
        # Support cache.set(old) syntax
        if isinstance(path, CdoCache): 
            enabled = path.enabled
            path = path.path

        self.path = path
        self.enabled = enabled
        self.old = old
        
        return old 
    
    def get(self):
        """
        Get the current cache path
        """
        return self.path

    def restore(self):
        """
        Restore the cache to its previous state
        """
        if self.old is None:
            raise ValueError("Cannot restore cache: no previous cache state saved")

        self.path = self.old.path
        self.enabled = self.old.enabled
        self.old = self.old.old


    def disable(self):
        """
        Disable caching

        Returns
        -------
        CdoCache
            The previous state of the cache
        """
        old = self._clone()
        self.enabled = False
        self.old = old
        return old

    def enable(self):
        """
        Enable caching

        Returns
        -------
        CdoCache
            The previous state of the cache
        """        
        if self.path is None:
            self.path = tempfile.mkdtemp()
        old = self._clone()
        self.enabled = True
        self.old = old
        return old
    
    def is_enabled(self):
        """
        Checks if cache is enable

        Returns
        -------
        bool
            Logical indicating if the cache is enabled.
        """     
        return self.enabled


    def forget(self):
        """
        Delete all files from the current cache. 
        """
        restore = Path(self.path).exists
        if self.path is not None:
            shutil.rmtree(self.path)
        if restore:
            os.makedirs(self.path) 

    def _hash_get(self, file: str):
        # File is the full path because the user 
        # might be saving the file outside the cache folder
        file = file + ".hash"
        if Path(file).is_file():
            with open(file) as f:
                return f.readline()
            
        else:
            return ""
    
    def _hash_store(self, file: str, hash: str):
        hash_file = file + ".hash"
        if not Path(os.path.dirname(hash_file)).exists:
            os.makedirs(os.path.dirname(hash_file))

        with open(hash_file, "w") as f:
            f.write(hash)


# Global cache to use by the package
cdo_cache = CdoCache()