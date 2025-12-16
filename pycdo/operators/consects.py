
from ..cdo_operator import CdoOperator
inf=float("inf")
def consects(self, ):
    r"""
    CDO operator: consects
    """
    operator = CdoOperator(command="consects",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
