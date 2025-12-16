
from ..cdo_operator import CdoOperator
inf=float("inf")
def timcumsum(self, ):
    r"""
    CDO operator: timcumsum
    """
    operator = CdoOperator(command="timcumsum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
