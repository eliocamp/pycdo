
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasstd(self, ):
    r"""
    CDO operator: seasstd
    """
    operator = CdoOperator(command="seasstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
