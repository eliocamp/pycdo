
from ..cdo_operator import CdoOperator
inf=float("inf")
def showyear(self, ):
    r"""
    CDO operator: showyear
    """
    operator = CdoOperator(command="showyear",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
