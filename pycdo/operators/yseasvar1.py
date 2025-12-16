
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasvar1(self, ):
    r"""
    CDO operator: yseasvar1
    """
    operator = CdoOperator(command="yseasvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
