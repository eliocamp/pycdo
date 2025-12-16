
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhoursum(self, ):
    r"""
    CDO operator: yhoursum
    """
    operator = CdoOperator(command="yhoursum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
