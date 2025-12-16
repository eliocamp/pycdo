
from ..cdo_operator import CdoOperator
inf=float("inf")
def yeardiv(self, ifile2):
    r"""
    CDO operator: yeardiv
    """
    operator = CdoOperator(command="yeardiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
