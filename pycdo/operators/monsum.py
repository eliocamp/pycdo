
from ..cdo_operator import CdoOperator
inf=float("inf")
def monsum(self, optional):
    r"""
    CDO operator: monsum
Parameters:
    optional: BOOL - Process the last month only if it is complete
    """
    operator = CdoOperator(command="monsum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
