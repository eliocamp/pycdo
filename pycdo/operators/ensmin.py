
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensmin(self, optional):
    r"""
    CDO operator: ensmin
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensmin",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
