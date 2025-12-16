
from ..cdo_operator import CdoOperator
inf=float("inf")
def seasmean(self, ):
    r"""
    CDO operator: seasmean
    """
    operator = CdoOperator(command="seasmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
