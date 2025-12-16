
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonstd1(self, ):
    r"""
    CDO operator: ymonstd1
    """
    operator = CdoOperator(command="ymonstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
