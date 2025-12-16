
from ..cdo_operator import CdoOperator
inf=float("inf")
def map(self, ):
    r"""
    CDO operator: map
    """
    operator = CdoOperator(command="map",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
