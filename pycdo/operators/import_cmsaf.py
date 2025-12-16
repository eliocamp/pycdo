
from ..cdo_operator import CdoOperator
inf=float("inf")
def import_cmsaf(self, ):
    r"""
    CDO operator: import_cmsaf
    """
    operator = CdoOperator(command="import_cmsaf",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
