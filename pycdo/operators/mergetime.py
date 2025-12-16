
from ..cdo_operator import CdoOperator
inf=float("inf")
def mergetime(self, optional):
    r"""
    CDO operator: mergetime
Parameters:
    optional: ['BOOL - Skips all consecutive timesteps with a double entry of the same timestamp.', 'STRING - Fill missing variable names with missing values (union) or use the intersection (intersect).']
    """
    operator = CdoOperator(command="mergetime",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
