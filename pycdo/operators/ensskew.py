
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensskew(self, optional):
    r"""
    CDO operator: ensskew
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensskew",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
