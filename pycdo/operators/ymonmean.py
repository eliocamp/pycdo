
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonmean(self, ):
    r"""
    CDO operator: ymonmean
    """
    operator = CdoOperator(command="ymonmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
