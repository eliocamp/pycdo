
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensstd1(self, optional):
    r"""
    CDO operator: ensstd1
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensstd1",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
