
from ..cdo_operator import CdoOperator
inf=float("inf")
def gheight_half(self, ):
    r"""
    CDO operator: gheight_half
    """
    operator = CdoOperator(command="gheight_half",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
