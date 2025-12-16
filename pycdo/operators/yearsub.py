
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearsub(self, ifile2):
    r"""
    CDO operator: yearsub
    """
    operator = CdoOperator(command="yearsub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
