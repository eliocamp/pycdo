
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourmean(self, ):
    r"""
    CDO operator: yhourmean
    """
    operator = CdoOperator(command="yhourmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
