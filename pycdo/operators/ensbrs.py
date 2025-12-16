
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensbrs(self, ):
    r"""
    CDO operator: ensbrs
    """
    operator = CdoOperator(command="ensbrs",
                           n_input=inf, 
                           n_output=inf, 
                           params=[])
    return self._new_op(operator, [], {})
