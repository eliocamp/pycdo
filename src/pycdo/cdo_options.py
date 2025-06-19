class CdoOptions:
    def __init__(self):
        self._options = None

    def set(self, options):
        """Set default CDO options (string or list of strings)."""
        old = self._options
        self._options = options
        return old

    def get(self):
        """Get current default CDO options."""
        return self._options
        
    def clear(self):
        old = self._options
        self._options = None
        return old

# Create a global options object
cdo_options = CdoOptions()