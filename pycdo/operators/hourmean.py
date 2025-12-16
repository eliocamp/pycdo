
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourmean(self, ):
    r"""
    CDO operator: hourmean
    """
    operator = CdoOperator(command="hourmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
