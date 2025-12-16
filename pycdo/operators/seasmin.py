
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasmin(self, ):
    r"""
    CDO operator: seasmin
    """
    operator = CdoOperator(command="seasmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
