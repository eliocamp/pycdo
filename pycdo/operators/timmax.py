
from ..cdo_operator import CdoOperator
inf=float("inf")
def timmax(self, ):
    r"""
    CDO operator: timmax
    """
    operator = CdoOperator(command="timmax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
