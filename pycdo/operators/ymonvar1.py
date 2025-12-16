
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonvar1(self, ):
    r"""
    CDO operator: ymonvar1
    """
    operator = CdoOperator(command="ymonvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
