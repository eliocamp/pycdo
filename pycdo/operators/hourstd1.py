
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourstd1(self, ):
    r"""
    CDO operator: hourstd1
    """
    operator = CdoOperator(command="hourstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
