
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhourstd1(self, ):
    r"""
    CDO operator: dhourstd1
    """
    operator = CdoOperator(command="dhourstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
