
from ..cdo_operator import CdoOperator
inf=float("inf")
def timmaxidx(self, ):
    r"""
    CDO operator: timmaxidx
    """
    operator = CdoOperator(command="timmaxidx",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
