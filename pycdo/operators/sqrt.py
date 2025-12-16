
from ..cdo_operator import CdoOperator
inf=float("inf")
def sqrt(self, ):
    r"""
    CDO operator: sqrt
    """
    operator = CdoOperator(command="sqrt",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
