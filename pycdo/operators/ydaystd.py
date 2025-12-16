
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaystd(self, ):
    r"""
    CDO operator: ydaystd
    """
    operator = CdoOperator(command="ydaystd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
