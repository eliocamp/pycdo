
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaymean(self, ):
    r"""
    CDO operator: ydaymean
    """
    operator = CdoOperator(command="ydaymean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
