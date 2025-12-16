
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutemax(self, ):
    r"""
    CDO operator: dminutemax
    """
    operator = CdoOperator(command="dminutemax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
