
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhourrange(self, ):
    r"""
    CDO operator: dhourrange
    """
    operator = CdoOperator(command="dhourrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
