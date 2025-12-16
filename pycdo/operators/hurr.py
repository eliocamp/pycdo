
from ..cdo_operator import CdoOperator
inf=float("inf")
def hurr(self, ):
    r"""
    CDO operator: hurr
    """
    operator = CdoOperator(command="hurr",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
