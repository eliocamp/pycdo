
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutesum(self, ):
    r"""
    CDO operator: dminutesum
    """
    operator = CdoOperator(command="dminutesum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
