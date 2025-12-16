
from ..cdo_operator import CdoOperator
inf=float("inf")
def enssum(self, optional):
    r"""
    CDO operator: enssum
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="enssum",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
