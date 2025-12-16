
from ..cdo_operator import CdoOperator
inf=float("inf")
def ensroc(self, ):
    r"""
    CDO operator: ensroc
    """
    operator = CdoOperator(command="ensroc",
                           n_input=inf, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
