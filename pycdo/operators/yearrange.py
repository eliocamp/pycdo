
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearrange(self, optional):
    r"""
    CDO operator: yearrange
Parameters:
    optional: BOOL - Process the last year only if it is complete
    """
    operator = CdoOperator(command="yearrange",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
