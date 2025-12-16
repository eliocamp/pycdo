
from ..cdo_operator import CdoOperator
inf=float("inf")
def zaxisdes(self, ):
    r"""
    CDO operator: zaxisdes
    """
    operator = CdoOperator(command="zaxisdes",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
