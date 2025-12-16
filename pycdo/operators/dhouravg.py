
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhouravg(self, ):
    r"""
    CDO operator: dhouravg
    """
    operator = CdoOperator(command="dhouravg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
