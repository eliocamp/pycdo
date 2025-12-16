
from ..cdo_operator import CdoOperator
inf=float("inf")
def consecsum(self, ):
    r"""
    CDO operator: consecsum
    """
    operator = CdoOperator(command="consecsum",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
