
from ..cdo_operator import CdoOperator
inf=float("inf")
def ndate(self, ):
    r"""
    CDO operator: ndate
    """
    operator = CdoOperator(command="ndate",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
