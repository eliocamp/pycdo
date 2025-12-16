
from ..cdo_operator import CdoOperator
inf=float("inf")
def daysub(self, ifile2):
    r"""
    CDO operator: daysub
    """
    operator = CdoOperator(command="daysub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
