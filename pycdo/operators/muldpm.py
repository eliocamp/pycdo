
from ..cdo_operator import CdoOperator
inf=float("inf")
def muldpm(self, ):
    r"""
    CDO operator: muldpm
    """
    operator = CdoOperator(command="muldpm",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
