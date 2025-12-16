
from ..cdo_operator import CdoOperator
inf=float("inf")
def ifthenc(self, optional):
    r"""
    CDO operator: ifthenc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="ifthenc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
