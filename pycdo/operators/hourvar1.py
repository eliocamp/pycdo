
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourvar1(self, ):
    r"""
    CDO operator: hourvar1
    """
    operator = CdoOperator(command="hourvar1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
