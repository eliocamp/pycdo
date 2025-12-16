
from ..cdo_operator import CdoOperator
inf=float("inf")
def gridboxstd1(self, optional):
    r"""
    CDO operator: gridboxstd1
Parameters:
    optional: ['INTEGER - Number of grid boxes in x direction', 'INTEGER - Number of grid boxes in y direction']
    """
    operator = CdoOperator(command="gridboxstd1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
