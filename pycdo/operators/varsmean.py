
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsmean(self, ):
    r"""
    CDO operator: varsmean
    """
    operator = CdoOperator(command="varsmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
