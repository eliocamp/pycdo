
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasstd(self, ):
    r"""
    CDO operator: yseasstd
    """
    operator = CdoOperator(command="yseasstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
