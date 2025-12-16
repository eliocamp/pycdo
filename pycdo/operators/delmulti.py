
from ..cdo_operator import CdoOperator
inf=float("inf")
def delmulti(self, ):
    r"""
    CDO operator: delmulti
    """
    operator = CdoOperator(command="delmulti",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
