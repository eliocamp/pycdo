
from ..cdo_operator import CdoOperator
inf=float("inf")
def trend(self, optional):
    r"""
    CDO operator: trend
Parameters:
    optional: BOOL - Set to false for unequal distributed timesteps (default: true)
    """
    operator = CdoOperator(command="trend",
                           n_input=1, 
                           n_output=2, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
