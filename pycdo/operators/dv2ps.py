
from ..cdo_operator import CdoOperator
inf=float("inf")
def dv2ps(self, ):
    r"""
    CDO operator: dv2ps
    """
    operator = CdoOperator(command="dv2ps",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
