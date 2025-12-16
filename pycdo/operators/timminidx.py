
from ..cdo_operator import CdoOperator
inf=float("inf")
def timminidx(self, ):
    r"""
    CDO operator: timminidx
    """
    operator = CdoOperator(command="timminidx",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
