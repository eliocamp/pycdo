
from ..cdo_operator import CdoOperator
inf=float("inf")
def showcode(self, ):
    r"""
    CDO operator: showcode
    """
    operator = CdoOperator(command="showcode",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
