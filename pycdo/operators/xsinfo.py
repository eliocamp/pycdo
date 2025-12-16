
from ..cdo_operator import CdoOperator
inf=float("inf")
def xsinfo(self, ):
    r"""
    CDO operator: xsinfo
    """
    operator = CdoOperator(command="xsinfo",
                           n_input=inf, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
