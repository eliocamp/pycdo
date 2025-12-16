
from ..cdo_operator import CdoOperator
inf=float("inf")
def merrange(self, optional):
    r"""
    CDO operator: merrange
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="merrange",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
