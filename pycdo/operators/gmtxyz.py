
from ..cdo_operator import CdoOperator
inf=float("inf")
def gmtxyz(self, ):
    r"""
    CDO operator: gmtxyz
    """
    operator = CdoOperator(command="gmtxyz",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
