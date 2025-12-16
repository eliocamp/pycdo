
from ..cdo_operator import CdoOperator
inf=float("inf")
def cat(self, ):
    r"""
    CDO operator: cat
    """
    operator = CdoOperator(command="cat",
                           n_input=inf, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
