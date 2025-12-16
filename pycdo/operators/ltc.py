
from ..cdo_operator import CdoOperator
inf=float("inf")
def ltc(self, optional):
    r"""
    CDO operator: ltc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="ltc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
