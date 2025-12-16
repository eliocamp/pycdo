
from ..cdo_operator import CdoOperator
inf=float("inf")
def dhourvar(self, ):
    r"""
    CDO operator: dhourvar
    """
    operator = CdoOperator(command="dhourvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
