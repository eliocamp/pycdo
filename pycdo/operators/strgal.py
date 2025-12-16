
from ..cdo_operator import CdoOperator
inf=float("inf")
def strgal(self, ):
    r"""
    CDO operator: strgal
    """
    operator = CdoOperator(command="strgal",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
