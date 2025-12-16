
from ..cdo_operator import CdoOperator
inf=float("inf")
def vertavg(self, optional):
    r"""
    CDO operator: vertavg
Parameters:
    optional: BOOL - weights=FALSE disables weighting by layer thickness \[default: weights=TRUE\]
    """
    operator = CdoOperator(command="vertavg",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
