
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaydiv(self, ifile2):
    r"""
    CDO operator: ydaydiv
    """
    operator = CdoOperator(command="ydaydiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
