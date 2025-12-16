
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasstd1(self, ):
    r"""
    CDO operator: seasstd1
    """
    operator = CdoOperator(command="seasstd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
