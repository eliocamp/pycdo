
from ..cdo_operator import CdoOperator
inf=float("inf")
def timsort(self, ):
    r"""
    CDO operator: timsort
    """
    operator = CdoOperator(command="timsort",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
