
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhourstd(self, ):
    r"""
    CDO operator: dhourstd
    """
    operator = CdoOperator(command="dhourstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
