
from ..cdo_operator import CdoOperator
inf=float("inf")
def sinfo(self, ):
    r"""
    CDO operator: sinfo
    """
    operator = CdoOperator(command="sinfo",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
