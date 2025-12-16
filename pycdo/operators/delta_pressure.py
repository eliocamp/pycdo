
from ..cdo_operator import CdoOperator
inf=float("inf")
def delta_pressure(self, ):
    r"""
    CDO operator: delta_pressure
    """
    operator = CdoOperator(command="delta_pressure",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
