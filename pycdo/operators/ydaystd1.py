
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaystd1(self, ):
    r"""
    CDO operator: ydaystd1
    """
    operator = CdoOperator(command="ydaystd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
