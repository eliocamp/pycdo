
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasvar1(self, ):
    r"""
    CDO operator: seasvar1
    """
    operator = CdoOperator(command="seasvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
