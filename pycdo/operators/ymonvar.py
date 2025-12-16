
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonvar(self, ):
    r"""
    CDO operator: ymonvar
    """
    operator = CdoOperator(command="ymonvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
