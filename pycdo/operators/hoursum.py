
from ..cdo_operator import CdoOperator
inf=float("inf")
def hoursum(self, ):
    r"""
    CDO operator: hoursum
    """
    operator = CdoOperator(command="hoursum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
