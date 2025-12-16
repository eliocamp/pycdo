
from ..cdo_operator import CdoOperator
inf=float("inf")
def subtrend(self, ifile2, ifile3, optional):
    r"""
    CDO operator: subtrend
Parameters:
    optional: BOOL - Set to false for unequal distributed timesteps (default: true)
    """
    operator = CdoOperator(command="subtrend",
                           n_input=3, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2, ifile3], {"optional": optional})
