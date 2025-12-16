
from ..cdo_operator import CdoOperator
inf=float("inf")
def gridboxkurt(self, optional):
    r"""
    CDO operator: gridboxkurt
Parameters:
    optional: ['INTEGER - Number of grid boxes in x direction', 'INTEGER - Number of grid boxes in y direction']
    """
    operator = CdoOperator(command="gridboxkurt",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
