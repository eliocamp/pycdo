
from ..cdo_operator import CdoOperator
inf=float("inf")
def deltat(self, ):
    r"""
    CDO operator: deltat
    """
    operator = CdoOperator(command="deltat",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
