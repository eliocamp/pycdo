
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearmul(self, ifile2):
    r"""
    CDO operator: yearmul
    """
    operator = CdoOperator(command="yearmul",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
