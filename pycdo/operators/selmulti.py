
from ..cdo_operator import CdoOperator
inf=float("inf")
def selmulti(self, ):
    r"""
    CDO operator: selmulti
    """
    operator = CdoOperator(command="selmulti",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
