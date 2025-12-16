
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseasdiv(self, ifile2):
    r"""
    CDO operator: yseasdiv
    """
    operator = CdoOperator(command="yseasdiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
