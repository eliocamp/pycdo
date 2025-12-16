
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensrkhistspace(self, ):
    r"""
    CDO operator: ensrkhistspace
    """
    operator = CdoOperator(command="ensrkhistspace",
                           n_input=inf, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
