
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutevar1(self, ):
    r"""
    CDO operator: dminutevar1
    """
    operator = CdoOperator(command="dminutevar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
