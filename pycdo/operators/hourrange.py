
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourrange(self, ):
    r"""
    CDO operator: hourrange
    """
    operator = CdoOperator(command="hourrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
