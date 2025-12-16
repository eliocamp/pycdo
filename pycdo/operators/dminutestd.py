
from ..cdo_operator import CdoOperator
inf=float("inf")
def dminutestd(self, ):
    r"""
    CDO operator: dminutestd
    """
    operator = CdoOperator(command="dminutestd",
                           n_input=1, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [], {})
