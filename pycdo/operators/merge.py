
from ..cdo_operator import CdoOperator
inf=float("inf")
def merge(self, optional):
    r"""
    CDO operator: merge
Parameters:
    optional: ['BOOL - Skips all consecutive timesteps with a double entry of the same timestamp.', 'STRING - Fill missing variable names with missing values (union) or use the intersection (intersect).']
    """
    operator = CdoOperator(command="merge",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
