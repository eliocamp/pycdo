
from ..cdo_operator import CdoOperator
inf=float("inf")
def houravg(self, ):
    r"""
    CDO operator: houravg
    """
    operator = CdoOperator(command="houravg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
