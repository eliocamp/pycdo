
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseassum(self, ):
    r"""
    CDO operator: yseassum
    """
    operator = CdoOperator(command="yseassum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
