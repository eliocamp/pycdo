
from ..cdo_operator import CdoOperator
inf=float("inf")
def rhopot(self, optional):
    r"""
    CDO operator: rhopot
Parameters:
    optional: FLOAT - Pressure in bar (constant value assigned to all levels)
    """
    operator = CdoOperator(command="rhopot",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
