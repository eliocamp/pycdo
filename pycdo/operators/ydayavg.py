
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydayavg(self, ):
    r"""
    CDO operator: ydayavg
    """
    operator = CdoOperator(command="ydayavg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
