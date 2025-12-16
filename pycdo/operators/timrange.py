
from ..cdo_operator import CdoOperator
inf=float("inf")
def timrange(self, ):
    r"""
    CDO operator: timrange
    """
    operator = CdoOperator(command="timrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
