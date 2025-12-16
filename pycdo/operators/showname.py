
from ..cdo_operator import CdoOperator
inf=float("inf")
def showname(self, ):
    r"""
    CDO operator: showname
    """
    operator = CdoOperator(command="showname",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
