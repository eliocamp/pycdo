
from ..cdo_operator import CdoOperator
inf=float("inf")
def negate(self, ):
    r"""
    CDO operator: negate
    """
    operator = CdoOperator(command="negate",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
