
from ..cdo_operator import CdoOperator
inf=float("inf")
def ap2pl(self, optional):
    r"""
    CDO operator: ap2pl
Parameters:
    optional: FLOAT - Comma-separated list of pressure levels in pascal
    """
    operator = CdoOperator(command="ap2pl",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
