
from ..cdo_operator import CdoOperator
inf=float("inf")
def sealevelpressure(self, ):
    r"""
    CDO operator: sealevelpressure
    """
    operator = CdoOperator(command="sealevelpressure",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
