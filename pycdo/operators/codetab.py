
from ..cdo_operator import CdoOperator
inf=float("inf")
def codetab(self, ):
    r"""
    CDO operator: codetab
    """
    operator = CdoOperator(command="codetab",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
