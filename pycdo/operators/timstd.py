
from ..cdo_operator import CdoOperator
inf=float("inf")
def timstd(self, ):
    r"""
    CDO operator: timstd
    """
    operator = CdoOperator(command="timstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
