
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminuteavg(self, ):
    r"""
    CDO operator: dminuteavg
    """
    operator = CdoOperator(command="dminuteavg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
