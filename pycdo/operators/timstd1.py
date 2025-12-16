
from ..cdo_operator import CdoOperator
inf=float("inf")
def timstd1(self, ):
    r"""
    CDO operator: timstd1
    """
    operator = CdoOperator(command="timstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
