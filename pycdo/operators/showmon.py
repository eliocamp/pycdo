
from ..cdo_operator import CdoOperator
inf=float("inf")
def showmon(self, ):
    r"""
    CDO operator: showmon
    """
    operator = CdoOperator(command="showmon",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
