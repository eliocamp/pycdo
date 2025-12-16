
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutemin(self, ):
    r"""
    CDO operator: dminutemin
    """
    operator = CdoOperator(command="dminutemin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
