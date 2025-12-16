
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasrange(self, ):
    r"""
    CDO operator: seasrange
    """
    operator = CdoOperator(command="seasrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
