
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasvar(self, ):
    r"""
    CDO operator: seasvar
    """
    operator = CdoOperator(command="seasvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
