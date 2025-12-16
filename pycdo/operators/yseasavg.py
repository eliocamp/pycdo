
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasavg(self, ):
    r"""
    CDO operator: yseasavg
    """
    operator = CdoOperator(command="yseasavg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
