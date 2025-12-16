
from ..cdo_operator import CdoOperator
inf=float("inf")
def sinfon(self, ):
    r"""
    CDO operator: sinfon
    """
    operator = CdoOperator(command="sinfon",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
