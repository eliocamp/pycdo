
from ..cdo_operator import CdoOperator
inf=float("inf")
def histmean(self, optional):
    r"""
    CDO operator: histmean
Parameters:
    optional: FLOAT - Comma-separated list of the bin bounds (-inf and inf valid)
    """
    operator = CdoOperator(command="histmean",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
