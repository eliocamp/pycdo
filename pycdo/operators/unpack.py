
from ..cdo_operator import CdoOperator
inf=float("inf")
def unpack(self, ):
    r"""
    CDO operator: unpack
    """
    operator = CdoOperator(command="unpack",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
