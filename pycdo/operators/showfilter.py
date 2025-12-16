
from ..cdo_operator import CdoOperator
inf=float("inf")
def showfilter(self, ):
    r"""
    CDO operator: showfilter
    """
    operator = CdoOperator(command="showfilter",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
