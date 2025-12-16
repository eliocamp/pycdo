
from ..cdo_operator import CdoOperator
inf=float("inf")
def ntime(self, ):
    r"""
    CDO operator: ntime
    """
    operator = CdoOperator(command="ntime",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
