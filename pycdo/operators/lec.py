
from ..cdo_operator import CdoOperator
inf=float("inf")
def lec(self, optional):
    r"""
    CDO operator: lec
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="lec",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
