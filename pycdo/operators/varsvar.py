
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsvar(self, ):
    r"""
    CDO operator: varsvar
    """
    operator = CdoOperator(command="varsvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
