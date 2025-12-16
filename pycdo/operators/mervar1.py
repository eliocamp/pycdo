
from ..cdo_operator import CdoOperator
inf=float("inf")
def mervar1(self, optional):
    r"""
    CDO operator: mervar1
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="mervar1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
