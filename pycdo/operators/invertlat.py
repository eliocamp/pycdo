
from ..cdo_operator import CdoOperator
inf=float("inf")
def invertlat(self, ):
    r"""
    CDO operator: invertlat
    """
    operator = CdoOperator(command="invertlat",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
