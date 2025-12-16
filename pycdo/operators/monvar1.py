
from ..cdo_operator import CdoOperator
inf=float("inf")
def monvar1(self, optional):
    r"""
    CDO operator: monvar1
Parameters:
    optional: BOOL - Process the last month only if it is complete
    """
    operator = CdoOperator(command="monvar1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
