
from ..cdo_operator import CdoOperator
inf=float("inf")
def vertvar1(self, optional):
    r"""
    CDO operator: vertvar1
Parameters:
    optional: BOOL - weights=FALSE disables weighting by layer thickness \[default: weights=TRUE\]
    """
    operator = CdoOperator(command="vertvar1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
