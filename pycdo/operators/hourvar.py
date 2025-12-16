
from ..cdo_operator import CdoOperator
inf=float("inf")
def hourvar(self, ):
    r"""
    CDO operator: hourvar
    """
    operator = CdoOperator(command="hourvar",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
