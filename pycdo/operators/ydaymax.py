
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaymax(self, ):
    r"""
    CDO operator: ydaymax
    """
    operator = CdoOperator(command="ydaymax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
