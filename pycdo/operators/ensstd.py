
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensstd(self, optional):
    r"""
    CDO operator: ensstd
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensstd",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
