
from ..cdo_operator import CdoOperator
inf=float("inf")
def import_amsr(self, ):
    r"""
    CDO operator: import_amsr
    """
    operator = CdoOperator(command="import_amsr",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
