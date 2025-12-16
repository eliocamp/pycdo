
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonmin(self, ):
    r"""
    CDO operator: ymonmin
    """
    operator = CdoOperator(command="ymonmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
