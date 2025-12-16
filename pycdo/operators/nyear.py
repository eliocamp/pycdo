
from ..cdo_operator import CdoOperator
inf=float("inf")
def nyear(self, ):
    r"""
    CDO operator: nyear
    """
    operator = CdoOperator(command="nyear",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
