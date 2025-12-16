
from ..cdo_operator import CdoOperator
inf=float("inf")
def isosurface(self, optional):
    r"""
    CDO operator: isosurface
Parameters:
    optional: FLOAT - Isosurface value
    """
    operator = CdoOperator(command="isosurface",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
