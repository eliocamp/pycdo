
from ..cdo_operator import CdoOperator
inf=float("inf")
def subc(self, optional):
    r"""
    CDO operator: subc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="subc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
