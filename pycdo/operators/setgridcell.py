
from ..cdo_operator import CdoOperator
inf=float("inf")
def setgridcell(self, optional):
    r"""
    CDO operator: setgridcell
Parameters:
    optional: ['FLOAT - Value of the grid cell', 'INTEGER - Comma-separated list of grid cell indices', 'STRING - Name of the data file which contains the mask']
    """
    operator = CdoOperator(command="setgridcell",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
