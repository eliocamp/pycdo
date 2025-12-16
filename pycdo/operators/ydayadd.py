
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydayadd(self, ifile2):
    r"""
    CDO operator: ydayadd
    """
    operator = CdoOperator(command="ydayadd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
