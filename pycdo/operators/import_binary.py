
from ..cdo_operator import CdoOperator
inf=float("inf")
def import_binary(self, ):
    r"""
    CDO operator: import_binary
    """
    operator = CdoOperator(command="import_binary",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
