
from ..cdo_operator import CdoOperator
inf=float("inf")
def infon(self, ):
    r"""
    CDO operator: infon
    """
    operator = CdoOperator(command="infon",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
