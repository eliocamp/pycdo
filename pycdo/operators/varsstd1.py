
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsstd1(self, ):
    r"""
    CDO operator: varsstd1
    """
    operator = CdoOperator(command="varsstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
