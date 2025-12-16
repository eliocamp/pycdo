
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonstd(self, ):
    r"""
    CDO operator: ymonstd
    """
    operator = CdoOperator(command="ymonstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
