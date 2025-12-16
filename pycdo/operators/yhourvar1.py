
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourvar1(self, ):
    r"""
    CDO operator: yhourvar1
    """
    operator = CdoOperator(command="yhourvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
