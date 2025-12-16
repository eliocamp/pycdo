
from ..cdo_operator import CdoOperator
inf=float("inf")
def partab(self, ):
    r"""
    CDO operator: partab
    """
    operator = CdoOperator(command="partab",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
