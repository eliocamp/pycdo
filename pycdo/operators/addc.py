
from ..cdo_operator import CdoOperator
inf=float("inf")
def addc(self, optional):
    r"""
    CDO operator: addc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="addc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
