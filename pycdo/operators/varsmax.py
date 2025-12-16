
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsmax(self, ):
    r"""
    CDO operator: varsmax
    """
    operator = CdoOperator(command="varsmax",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
