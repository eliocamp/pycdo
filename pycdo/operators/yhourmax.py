
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourmax(self, ):
    r"""
    CDO operator: yhourmax
    """
    operator = CdoOperator(command="yhourmax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
