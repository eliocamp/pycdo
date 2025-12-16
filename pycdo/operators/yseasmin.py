
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasmin(self, ):
    r"""
    CDO operator: yseasmin
    """
    operator = CdoOperator(command="yseasmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
