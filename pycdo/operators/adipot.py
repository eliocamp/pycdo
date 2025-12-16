
from ..cdo_operator import CdoOperator
inf=float("inf")
def adipot(self, optional):
    r"""
    CDO operator: adipot
Parameters:
    optional: FLOAT - Pressure in bar (constant value assigned to all levels)
    """
    operator = CdoOperator(command="adipot",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
