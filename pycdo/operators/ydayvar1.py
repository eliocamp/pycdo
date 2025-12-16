
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydayvar1(self, ):
    r"""
    CDO operator: ydayvar1
    """
    operator = CdoOperator(command="ydayvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
