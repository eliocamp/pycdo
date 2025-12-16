
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaymin(self, ):
    r"""
    CDO operator: ydaymin
    """
    operator = CdoOperator(command="ydaymin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
