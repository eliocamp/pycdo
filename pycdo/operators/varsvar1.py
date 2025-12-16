
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsvar1(self, ):
    r"""
    CDO operator: varsvar1
    """
    operator = CdoOperator(command="varsvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
