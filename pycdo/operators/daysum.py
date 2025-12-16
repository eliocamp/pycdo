
from ..cdo_operator import CdoOperator
inf=float("inf")
def daysum(self, optional):
    r"""
    CDO operator: daysum
Parameters:
    optional: BOOL - Process the last day only if it is complete
    """
    operator = CdoOperator(command="daysum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
