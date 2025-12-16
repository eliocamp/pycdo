
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasrange(self, ):
    r"""
    CDO operator: yseasrange
    """
    operator = CdoOperator(command="yseasrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
