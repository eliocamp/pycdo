
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutestd1(self, ):
    r"""
    CDO operator: dminutestd1
    """
    operator = CdoOperator(command="dminutestd1",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
