
from ..cdo_operator import CdoOperator
inf=float("inf")
def xsinfop(self, ):
    r"""
    CDO operator: xsinfop
    """
    operator = CdoOperator(command="xsinfop",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
