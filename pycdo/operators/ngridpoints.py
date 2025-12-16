
from ..cdo_operator import CdoOperator
inf=float("inf")
def ngridpoints(self, ):
    r"""
    CDO operator: ngridpoints
    """
    operator = CdoOperator(command="ngridpoints",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
