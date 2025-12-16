
from ..cdo_operator import CdoOperator
inf=float("inf")
def gridboxrange(self, optional):
    r"""
    CDO operator: gridboxrange
Parameters:
    optional: ['INTEGER - Number of grid boxes in x direction', 'INTEGER - Number of grid boxes in y direction']
    """
    operator = CdoOperator(command="gridboxrange",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
