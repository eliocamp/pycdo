
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsrange(self, ):
    r"""
    CDO operator: varsrange
    """
    operator = CdoOperator(command="varsrange",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
