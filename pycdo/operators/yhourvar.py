
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourvar(self, ):
    r"""
    CDO operator: yhourvar
    """
    operator = CdoOperator(command="yhourvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
