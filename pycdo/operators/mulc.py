
from ..cdo_operator import CdoOperator
inf=float("inf")
def mulc(self, optional):
    r"""
    CDO operator: mulc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="mulc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
