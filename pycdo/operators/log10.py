
from ..cdo_operator import CdoOperator
inf=float("inf")
def log10(self, ):
    r"""
    CDO operator: log10
    """
    operator = CdoOperator(command="log10",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
