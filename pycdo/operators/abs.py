
from ..cdo_operator import CdoOperator
inf=float("inf")
def abs(self, ):
    r"""
    CDO operator: abs
    """
    operator = CdoOperator(command="abs",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
