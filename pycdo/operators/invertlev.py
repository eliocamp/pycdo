
from ..cdo_operator import CdoOperator
inf=float("inf")
def invertlev(self, ):
    r"""
    CDO operator: invertlev
    """
    operator = CdoOperator(command="invertlev",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
