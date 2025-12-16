
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourstd(self, ):
    r"""
    CDO operator: hourstd
    """
    operator = CdoOperator(command="hourstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
