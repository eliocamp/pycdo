
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourmax(self, ):
    r"""
    CDO operator: hourmax
    """
    operator = CdoOperator(command="hourmax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
