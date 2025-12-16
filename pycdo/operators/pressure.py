
from ..cdo_operator import CdoOperator
inf=float("inf")
def pressure(self, ):
    r"""
    CDO operator: pressure
    """
    operator = CdoOperator(command="pressure",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
