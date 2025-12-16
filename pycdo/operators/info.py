
from ..cdo_operator import CdoOperator
inf=float("inf")
def info(self, ):
    r"""
    CDO operator: info
    """
    operator = CdoOperator(command="info",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
