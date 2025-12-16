
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonsub(self, ifile2):
    r"""
    CDO operator: ymonsub
    """
    operator = CdoOperator(command="ymonsub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
