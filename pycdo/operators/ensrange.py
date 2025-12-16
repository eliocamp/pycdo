
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensrange(self, optional):
    r"""
    CDO operator: ensrange
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensrange",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
