
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourstd1(self, ):
    r"""
    CDO operator: yhourstd1
    """
    operator = CdoOperator(command="yhourstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
