
from ..cdo_operator import CdoOperator
inf=float("inf")
def dayrange(self, optional):
    r"""
    CDO operator: dayrange
Parameters:
    optional: BOOL - Process the last day only if it is complete
    """
    operator = CdoOperator(command="dayrange",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
