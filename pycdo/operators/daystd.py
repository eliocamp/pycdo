
from ..cdo_operator import CdoOperator
inf=float("inf")
def daystd(self, optional):
    r"""
    CDO operator: daystd
Parameters:
    optional: BOOL - Process the last day only if it is complete
    """
    operator = CdoOperator(command="daystd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
