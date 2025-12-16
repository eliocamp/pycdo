
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensmean(self, optional):
    r"""
    CDO operator: ensmean
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensmean",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
