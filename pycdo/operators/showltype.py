
from ..cdo_operator import CdoOperator
inf=float("inf")
def showltype(self, ):
    r"""
    CDO operator: showltype
    """
    operator = CdoOperator(command="showltype",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
