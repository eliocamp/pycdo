
from ..cdo_operator import CdoOperator
inf=float("inf")
def vct(self, ):
    r"""
    CDO operator: vct
    """
    operator = CdoOperator(command="vct",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
