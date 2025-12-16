
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourmin(self, ):
    r"""
    CDO operator: hourmin
    """
    operator = CdoOperator(command="hourmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
