
from ..cdo_operator import CdoOperator
inf=float("inf")
def eqc(self, optional):
    r"""
    CDO operator: eqc
Parameters:
    optional: FLOAT - Constant
    """
    operator = CdoOperator(command="eqc",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
