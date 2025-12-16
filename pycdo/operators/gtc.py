
from ..cdo_operator import CdoOperator
inf=float("inf")
def gtc(self, optional):
    r"""
    CDO operator: gtc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="gtc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
