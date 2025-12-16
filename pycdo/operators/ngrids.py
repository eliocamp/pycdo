
from ..cdo_operator import CdoOperator
inf=float("inf")
def ngrids(self, ):
    r"""
    CDO operator: ngrids
    """
    operator = CdoOperator(command="ngrids",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
