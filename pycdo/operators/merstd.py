
from ..cdo_operator import CdoOperator
inf=float("inf")
def merstd(self, optional):
    r"""
    CDO operator: merstd
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="merstd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
