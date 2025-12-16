
from ..cdo_operator import CdoOperator
inf=float("inf")
def timsum(self, ):
    r"""
    CDO operator: timsum
    """
    operator = CdoOperator(command="timsum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
