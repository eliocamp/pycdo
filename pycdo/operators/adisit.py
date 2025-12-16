
from ..cdo_operator import CdoOperator
inf=float("inf")
def adisit(self, optional):
    r"""
    CDO operator: adisit
Parameters:
    optional: FLOAT - Pressure in bar (constant value assigned to all levels)
    """
    operator = CdoOperator(command="adisit",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
