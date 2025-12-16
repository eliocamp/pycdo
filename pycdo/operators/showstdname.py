
from ..cdo_operator import CdoOperator
inf=float("inf")
def showstdname(self, ):
    r"""
    CDO operator: showstdname
    """
    operator = CdoOperator(command="showstdname",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
