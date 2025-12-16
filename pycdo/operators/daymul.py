
from ..cdo_operator import CdoOperator
inf=float("inf")
def daymul(self, ifile2):
    r"""
    CDO operator: daymul
    """
    operator = CdoOperator(command="daymul",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
