
from ..cdo_operator import CdoOperator
inf=float("inf")
def merskew(self, optional):
    r"""
    CDO operator: merskew
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="merskew",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
