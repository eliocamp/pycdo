
from ..cdo_operator import CdoOperator
inf=float("inf")
def topvalue(self, optional):
    r"""
    CDO operator: topvalue
Parameters:
    optional: FLOAT - Isosurface value
    """
    operator = CdoOperator(command="topvalue",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
