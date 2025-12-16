
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhourmin(self, ):
    r"""
    CDO operator: dhourmin
    """
    operator = CdoOperator(command="dhourmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
