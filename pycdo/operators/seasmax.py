
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasmax(self, ):
    r"""
    CDO operator: seasmax
    """
    operator = CdoOperator(command="seasmax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
