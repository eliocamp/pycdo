
from ..cdo_operator import CdoOperator
inf=float("inf")
def mermax(self, optional):
    r"""
    CDO operator: mermax
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="mermax",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
