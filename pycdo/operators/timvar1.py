
from ..cdo_operator import CdoOperator
inf=float("inf")
def timvar1(self, ):
    r"""
    CDO operator: timvar1
    """
    operator = CdoOperator(command="timvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
