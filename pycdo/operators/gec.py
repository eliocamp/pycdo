
from ..cdo_operator import CdoOperator
inf=float("inf")
def gec(self, optional):
    r"""
    CDO operator: gec
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="gec",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
