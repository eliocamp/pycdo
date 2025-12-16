
from ..cdo_operator import CdoOperator
inf=float("inf")
def vertmax(self, optional):
    r"""
    CDO operator: vertmax
Parameters:
    optional: BOOL - weights=FALSE disables weighting by layer thickness \[default: weights=TRUE\]
    """
    operator = CdoOperator(command="vertmax",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
