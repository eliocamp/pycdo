
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasstd1(self, ):
    r"""
    CDO operator: yseasstd1
    """
    operator = CdoOperator(command="yseasstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
