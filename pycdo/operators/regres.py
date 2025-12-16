
from ..cdo_operator import CdoOperator
inf=float("inf")
def regres(self, optional):
    r"""
    CDO operator: regres
Parameters:
    optional: BOOL - Set to false for unequal distributed timesteps (default: true)
    """
    operator = CdoOperator(command="regres",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
