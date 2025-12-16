
from ..cdo_operator import CdoOperator
inf=float("inf")
def mulcoslat(self, ):
    r"""
    CDO operator: mulcoslat
    """
    operator = CdoOperator(command="mulcoslat",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
