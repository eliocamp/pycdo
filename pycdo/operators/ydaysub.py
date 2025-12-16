
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydaysub(self, ifile2):
    r"""
    CDO operator: ydaysub
    """
    operator = CdoOperator(command="ydaysub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
