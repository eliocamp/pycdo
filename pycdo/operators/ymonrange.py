
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonrange(self, ):
    r"""
    CDO operator: ymonrange
    """
    operator = CdoOperator(command="ymonrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
