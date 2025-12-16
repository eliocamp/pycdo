
from ..cdo_operator import CdoOperator
inf=float("inf")
def acos(self, ):
    r"""
    CDO operator: acos
    """
    operator = CdoOperator(command="acos",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
