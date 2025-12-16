
from ..cdo_operator import CdoOperator
inf=float("inf")
def splitdate(self, ):
    r"""
    CDO operator: splitdate
    """
    operator = CdoOperator(command="splitdate",
                           n_input=1, 
                           n_output=inf, 
                           params=[])
    return self._new_op(operator, [], {})
