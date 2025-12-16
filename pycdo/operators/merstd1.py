
from ..cdo_operator import CdoOperator
inf=float("inf")
def merstd1(self, optional):
    r"""
    CDO operator: merstd1
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="merstd1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
