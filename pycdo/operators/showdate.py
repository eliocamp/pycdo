
from ..cdo_operator import CdoOperator
inf=float("inf")
def showdate(self, ):
    r"""
    CDO operator: showdate
    """
    operator = CdoOperator(command="showdate",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
