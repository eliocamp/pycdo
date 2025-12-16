
from ..cdo_operator import CdoOperator
inf=float("inf")
def cos(self, ):
    r"""
    CDO operator: cos
    """
    operator = CdoOperator(command="cos",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
