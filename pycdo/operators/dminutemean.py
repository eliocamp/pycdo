
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutemean(self, ):
    r"""
    CDO operator: dminutemean
    """
    operator = CdoOperator(command="dminutemean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
