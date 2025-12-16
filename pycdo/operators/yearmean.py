
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearmean(self, optional):
    r"""
    CDO operator: yearmean
Parameters:
    optional: BOOL - Process the last year only if it is complete
    """
    operator = CdoOperator(command="yearmean",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
