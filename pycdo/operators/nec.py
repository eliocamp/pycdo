
from ..cdo_operator import CdoOperator
inf=float("inf")
def nec(self, optional):
    r"""
    CDO operator: nec
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="nec",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
