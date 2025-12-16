
from ..cdo_operator import CdoOperator
inf=float("inf")
def npar(self, ):
    r"""
    CDO operator: npar
    """
    operator = CdoOperator(command="npar",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
