
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonavg(self, ):
    r"""
    CDO operator: ymonavg
    """
    operator = CdoOperator(command="ymonavg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
