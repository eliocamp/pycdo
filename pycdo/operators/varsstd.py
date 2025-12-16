
from ..cdo_operator import CdoOperator
inf=float("inf")
def varsstd(self, ):
    r"""
    CDO operator: varsstd
    """
    operator = CdoOperator(command="varsstd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
