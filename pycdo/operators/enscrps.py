
from ..cdo_operator import CdoOperator
inf=float("inf")
def enscrps(self, ):
    r"""
    CDO operator: enscrps
    """
    operator = CdoOperator(command="enscrps",
                           n_input=inf, 
                           n_output=inf, 
                           params=[])
    return self._new_op(operator, [], {})
