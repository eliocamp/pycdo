
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonsum(self, ):
    r"""
    CDO operator: ymonsum
    """
    operator = CdoOperator(command="ymonsum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
