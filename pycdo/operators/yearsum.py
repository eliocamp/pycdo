
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearsum(self, optional):
    r"""
    CDO operator: yearsum
Parameters:
    optional: BOOL - Process the last year only if it is complete
    """
    operator = CdoOperator(command="yearsum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
