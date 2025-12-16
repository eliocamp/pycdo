
from ..cdo_operator import CdoOperator
inf=float("inf")
def copy(self, ):
    r"""
    CDO operator: copy
    """
    operator = CdoOperator(command="copy",
                           n_input=inf, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
