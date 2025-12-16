
from ..cdo_operator import CdoOperator
inf=float("inf")
def mastrfu(self, ):
    r"""
    CDO operator: mastrfu
    """
    operator = CdoOperator(command="mastrfu",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
