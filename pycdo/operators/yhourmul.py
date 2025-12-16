
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourmul(self, ifile2):
    r"""
    CDO operator: yhourmul
    """
    operator = CdoOperator(command="yhourmul",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
