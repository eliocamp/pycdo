
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaysum(self, ):
    r"""
    CDO operator: ydaysum
    """
    operator = CdoOperator(command="ydaysum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
