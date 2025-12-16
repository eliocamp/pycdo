
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensavg(self, optional):
    r"""
    CDO operator: ensavg
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensavg",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
