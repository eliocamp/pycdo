
from ..cdo_operator import CdoOperator
inf=float("inf")
def timvar(self, ):
    r"""
    CDO operator: timvar
    """
    operator = CdoOperator(command="timvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
