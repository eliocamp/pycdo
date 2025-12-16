
from ..cdo_operator import CdoOperator
inf=float("inf")
def exp(self, ):
    r"""
    CDO operator: exp
    """
    operator = CdoOperator(command="exp",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
