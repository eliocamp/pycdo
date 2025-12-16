
from ..cdo_operator import CdoOperator
inf=float("inf")
def varssum(self, ):
    r"""
    CDO operator: varssum
    """
    operator = CdoOperator(command="varssum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
