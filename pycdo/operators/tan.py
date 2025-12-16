
from ..cdo_operator import CdoOperator
inf=float("inf")
def tan(self, ):
    r"""
    CDO operator: tan
    """
    operator = CdoOperator(command="tan",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
