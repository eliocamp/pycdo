
from ..cdo_operator import CdoOperator
inf=float("inf")
def seassum(self, ):
    r"""
    CDO operator: seassum
    """
    operator = CdoOperator(command="seassum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
