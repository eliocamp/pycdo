
from ..cdo_operator import CdoOperator
inf=float("inf")
def divc(self, optional):
    r"""
    CDO operator: divc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="divc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
