
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonmean(self, ):
    """
    CDO operator: ymonmean
    """
    operator = CdoOperator(name="ymonmean",
                           num_inputs=1, 
                           num_outputs=1, 
                           parameters=[])
    return self._new_op(operator, [], {})
