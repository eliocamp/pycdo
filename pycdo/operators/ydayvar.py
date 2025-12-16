
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydayvar(self, ):
    r"""
    CDO operator: ydayvar
    """
    operator = CdoOperator(command="ydayvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
