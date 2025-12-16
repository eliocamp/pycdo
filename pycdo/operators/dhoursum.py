
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhoursum(self, ):
    r"""
    CDO operator: dhoursum
    """
    operator = CdoOperator(command="dhoursum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
