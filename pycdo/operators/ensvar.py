
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensvar(self, optional):
    r"""
    CDO operator: ensvar
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="ensvar",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
