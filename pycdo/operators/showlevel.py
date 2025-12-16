
from ..cdo_operator import CdoOperator
inf=float("inf")
def showlevel(self, ):
    r"""
    CDO operator: showlevel
    """
    operator = CdoOperator(command="showlevel",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
