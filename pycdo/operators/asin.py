
from ..cdo_operator import CdoOperator
inf=float("inf")
def asin(self, ):
    r"""
    CDO operator: asin
    """
    operator = CdoOperator(command="asin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
