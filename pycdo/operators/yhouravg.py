
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhouravg(self, ):
    r"""
    CDO operator: yhouravg
    """
    operator = CdoOperator(command="yhouravg",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
