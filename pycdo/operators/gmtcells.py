
from ..cdo_operator import CdoOperator
inf=float("inf")
def gmtcells(self, ):
    r"""
    CDO operator: gmtcells
    """
    operator = CdoOperator(command="gmtcells",
                           n_input=1, 
                           n_output=0, 
                           params=[])
    return self._new_op(operator, [], {})
