
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearvar1(self, optional):
    r"""
    CDO operator: yearvar1
Parameters:
    optional: BOOL - Process the last year only if it is complete
    """
    operator = CdoOperator(command="yearvar1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
