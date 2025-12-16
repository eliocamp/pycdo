
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourmin(self, ):
    r"""
    CDO operator: yhourmin
    """
    operator = CdoOperator(command="yhourmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
