
from ..cdo_operator import CdoOperator
inf=float("inf")
def selindexbox(self, optional):
    r"""
    CDO operator: selindexbox
Parameters:
    optional: ['FLOAT - Western longitude in degrees', 'FLOAT - Eastern longitude in degrees', 'FLOAT - Southern or northern latitude in degrees', 'FLOAT - Northern or southern latitude in degrees', 'INTEGER - Index of first longitude (1 - nlon)', 'INTEGER - Index of last longitude (1 - nlon)', 'INTEGER - Index of first latitude (1 - nlat)', 'INTEGER - Index of last latitude (1 - nlat)']
    """
    operator = CdoOperator(command="selindexbox",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
