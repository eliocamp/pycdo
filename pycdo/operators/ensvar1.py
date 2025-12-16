
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensvar1(self, optional):
    r"""
    CDO operator: ensvar1
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensvar1",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
