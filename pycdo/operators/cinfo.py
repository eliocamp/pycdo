
from ..cdo_operator import CdoOperator
inf=float("inf")
def cinfo(self, ):
    r"""
    CDO operator: cinfo
    """
    operator = CdoOperator(command="cinfo",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
