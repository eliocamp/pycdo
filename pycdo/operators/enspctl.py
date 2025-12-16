
from ..cdo_operator import CdoOperator
inf=float("inf")
def enspctl(self, optional):
    r"""
    CDO operator: enspctl
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="enspctl",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
