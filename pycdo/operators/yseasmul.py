
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasmul(self, ifile2):
    r"""
    CDO operator: yseasmul
    """
    operator = CdoOperator(command="yseasmul",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
