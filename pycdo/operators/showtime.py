
from ..cdo_operator import CdoOperator
inf=float("inf")
def showtime(self, ):
    r"""
    CDO operator: showtime
    """
    operator = CdoOperator(command="showtime",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
