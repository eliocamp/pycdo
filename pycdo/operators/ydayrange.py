
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydayrange(self, ):
    r"""
    CDO operator: ydayrange
    """
    operator = CdoOperator(command="ydayrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
