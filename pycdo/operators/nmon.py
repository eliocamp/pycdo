
from ..cdo_operator import CdoOperator
inf=float("inf")
def nmon(self, ):
    r"""
    CDO operator: nmon
    """
    operator = CdoOperator(command="nmon",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
