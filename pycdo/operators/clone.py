
from ..cdo_operator import CdoOperator
inf=float("inf")
def clone(self, ):
    r"""
    CDO operator: clone
    """
    operator = CdoOperator(command="clone",
                           n_input=inf, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
