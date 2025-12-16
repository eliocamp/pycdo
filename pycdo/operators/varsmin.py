
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsmin(self, ):
    r"""
    CDO operator: varsmin
    """
    operator = CdoOperator(command="varsmin",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
