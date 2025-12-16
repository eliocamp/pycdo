
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearmaxidx(self, optional):
    r"""
    CDO operator: yearmaxidx
Parameters:
    optional: BOOL - Process the last year only if it is complete
    """
    operator = CdoOperator(command="yearmaxidx",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
