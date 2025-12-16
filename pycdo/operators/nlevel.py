
from ..cdo_operator import CdoOperator
inf=float("inf")
def nlevel(self, ):
    r"""
    CDO operator: nlevel
    """
    operator = CdoOperator(command="nlevel",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
