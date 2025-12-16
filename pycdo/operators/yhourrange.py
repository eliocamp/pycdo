
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourrange(self, ):
    r"""
    CDO operator: yhourrange
    """
    operator = CdoOperator(command="yhourrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
