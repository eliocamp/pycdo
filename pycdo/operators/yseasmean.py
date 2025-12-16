
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasmean(self, ):
    r"""
    CDO operator: yseasmean
    """
    operator = CdoOperator(command="yseasmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
