
from ..cdo_operator import CdoOperator
inf=float("inf")
def timavg(self, ):
    r"""
    CDO operator: timavg
    """
    operator = CdoOperator(command="timavg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
