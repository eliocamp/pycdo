
from ..cdo_operator import CdoOperator
inf=float("inf")
def minc(self, optional):
    r"""
    CDO operator: minc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="minc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
