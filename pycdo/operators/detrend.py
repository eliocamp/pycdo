
from ..cdo_operator import CdoOperator
inf=float("inf")
def detrend(self, optional):
    r"""
    CDO operator: detrend
Parameters:
    optional: BOOL - Set to false for unequal distributed timesteps (default: true)
    """
    operator = CdoOperator(command="detrend",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
