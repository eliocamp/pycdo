
from ..cdo_operator import CdoOperator
inf=float("inf")
def nint(self, ):
    r"""
    CDO operator: nint
    """
    operator = CdoOperator(command="nint",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
