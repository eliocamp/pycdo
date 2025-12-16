
from ..cdo_operator import CdoOperator
inf=float("inf")
def daystd1(self, optional):
    r"""
    CDO operator: daystd1
Parameters:
    optional: BOOL - Process the last day only if it is complete
    """
    operator = CdoOperator(command="daystd1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
