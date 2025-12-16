
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensrkhisttime(self, ):
    r"""
    CDO operator: ensrkhisttime
    """
    operator = CdoOperator(command="ensrkhisttime",
                           n_input=inf, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
