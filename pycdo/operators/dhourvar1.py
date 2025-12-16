
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhourvar1(self, ):
    r"""
    CDO operator: dhourvar1
    """
    operator = CdoOperator(command="dhourvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
