
from ..cdo_operator import CdoOperator
inf=float("inf")
def meravg(self, optional):
    r"""
    CDO operator: meravg
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="meravg",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
