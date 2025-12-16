
from ..cdo_operator import CdoOperator
inf=float("inf")
def sin(self, ):
    r"""
    CDO operator: sin
    """
    operator = CdoOperator(command="sin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
