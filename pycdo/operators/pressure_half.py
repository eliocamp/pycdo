
from ..cdo_operator import CdoOperator
inf=float("inf")
def pressure_half(self, ):
    r"""
    CDO operator: pressure_half
    """
    operator = CdoOperator(command="pressure_half",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
