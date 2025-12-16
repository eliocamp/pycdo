
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasvar(self, ):
    r"""
    CDO operator: yseasvar
    """
    operator = CdoOperator(command="yseasvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
