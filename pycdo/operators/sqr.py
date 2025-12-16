
from ..cdo_operator import CdoOperator
inf=float("inf")
def sqr(self, ):
    r"""
    CDO operator: sqr
    """
    operator = CdoOperator(command="sqr",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
