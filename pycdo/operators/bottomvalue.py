
from ..cdo_operator import CdoOperator
inf=float("inf")
def bottomvalue(self, optional):
    r"""
    CDO operator: bottomvalue
Parameters:
    optional: FLOAT - Isosurface value
    """
    operator = CdoOperator(command="bottomvalue",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
