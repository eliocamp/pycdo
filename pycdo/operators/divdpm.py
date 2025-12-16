
from ..cdo_operator import CdoOperator
inf=float("inf")
def divdpm(self, ):
    r"""
    CDO operator: divdpm
    """
    operator = CdoOperator(command="divdpm",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
