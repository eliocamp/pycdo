
from ..cdo_operator import CdoOperator
inf=float("inf")
def divcoslat(self, ):
    r"""
    CDO operator: divcoslat
    """
    operator = CdoOperator(command="divcoslat",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
