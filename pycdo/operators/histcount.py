
from ..cdo_operator import CdoOperator
inf=float("inf")
def histcount(self, optional):
    r"""
    CDO operator: histcount
Parameters:
    optional: FLOAT - Comma-separated list of the bin bounds (-inf and inf valid)
    """
    operator = CdoOperator(command="histcount",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
