
from ..cdo_operator import CdoOperator
inf=float("inf")
def ifnotthenc(self, optional):
    r"""
    CDO operator: ifnotthenc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="ifnotthenc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
