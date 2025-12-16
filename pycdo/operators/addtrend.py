
from ..cdo_operator import CdoOperator
inf=float("inf")
def addtrend(self, ifile2, ifile3, optional):
    r"""
    CDO operator: addtrend
Parameters:
    optional: BOOL - Set to false for unequal distributed timesteps (default: true)
    """
    operator = CdoOperator(command="addtrend",
                           n_input=3, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2, ifile3], {"optional": optional})
