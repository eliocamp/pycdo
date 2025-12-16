
from ..cdo_operator import CdoOperator
inf=float("inf")
def daymin(self, optional):
    r"""
    CDO operator: daymin
Parameters:
    optional: BOOL - Process the last day only if it is complete
    """
    operator = CdoOperator(command="daymin",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
