
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaymul(self, ifile2):
    r"""
    CDO operator: ydaymul
    """
    operator = CdoOperator(command="ydaymul",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
