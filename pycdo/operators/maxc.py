
from ..cdo_operator import CdoOperator
inf=float("inf")
def maxc(self, optional):
    r"""
    CDO operator: maxc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="maxc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
