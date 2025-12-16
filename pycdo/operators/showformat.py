
from ..cdo_operator import CdoOperator
inf=float("inf")
def showformat(self, ):
    r"""
    CDO operator: showformat
    """
    operator = CdoOperator(command="showformat",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
