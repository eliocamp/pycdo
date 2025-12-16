
from ..cdo_operator import CdoOperator
inf=float("inf")
def ln(self, ):
    r"""
    CDO operator: ln
    """
    operator = CdoOperator(command="ln",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
