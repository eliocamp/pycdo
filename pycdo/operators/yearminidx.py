
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearminidx(self, optional):
    r"""
    CDO operator: yearminidx
Parameters:
    optional: BOOL - Process the last year only if it is complete
    """
    operator = CdoOperator(command="yearminidx",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
