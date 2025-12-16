
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasavg(self, ):
    r"""
    CDO operator: seasavg
    """
    operator = CdoOperator(command="seasavg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
