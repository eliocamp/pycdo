
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonmax(self, ):
    r"""
    CDO operator: ymonmax
    """
    operator = CdoOperator(command="ymonmax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
