
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourstd(self, ):
    r"""
    CDO operator: yhourstd
    """
    operator = CdoOperator(command="yhourstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
