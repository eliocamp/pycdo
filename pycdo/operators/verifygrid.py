
from ..cdo_operator import CdoOperator
inf=float("inf")
def verifygrid(self, ):
    r"""
    CDO operator: verifygrid
    """
    operator = CdoOperator(command="verifygrid",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
