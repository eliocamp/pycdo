
from ..cdo_operator import CdoOperator
inf=float("inf")
def atan(self, ):
    r"""
    CDO operator: atan
    """
    operator = CdoOperator(command="atan",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
