
from ..cdo_operator import CdoOperator
inf=float("inf")
def showtimestamp(self, ):
    r"""
    CDO operator: showtimestamp
    """
    operator = CdoOperator(command="showtimestamp",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
