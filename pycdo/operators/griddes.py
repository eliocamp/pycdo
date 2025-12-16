
from ..cdo_operator import CdoOperator
inf=float("inf")
def griddes(self, ):
    r"""
    CDO operator: griddes
    """
    operator = CdoOperator(command="griddes",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
