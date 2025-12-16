
from ..cdo_operator import CdoOperator
inf=float("inf")
def timmin(self, ):
    r"""
    CDO operator: timmin
    """
    operator = CdoOperator(command="timmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
