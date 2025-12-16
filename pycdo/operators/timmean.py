
from ..cdo_operator import CdoOperator
inf=float("inf")
def timmean(self, ):
    r"""
    CDO operator: timmean
    """
    operator = CdoOperator(command="timmean",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
