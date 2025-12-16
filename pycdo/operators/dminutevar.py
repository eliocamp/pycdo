
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutevar(self, ):
    r"""
    CDO operator: dminutevar
    """
    operator = CdoOperator(command="dminutevar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
