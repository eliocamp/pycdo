
from ..cdo_operator import CdoOperator
inf=float("inf")
def divdpy(self, ):
    r"""
    CDO operator: divdpy
    """
    operator = CdoOperator(command="divdpy",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
