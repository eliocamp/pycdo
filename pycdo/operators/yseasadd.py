
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasadd(self, ifile2):
    r"""
    CDO operator: yseasadd
    """
    operator = CdoOperator(command="yseasadd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
