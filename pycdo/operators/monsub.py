
from ..cdo_operator import CdoOperator
inf=float("inf")
def monsub(self, ifile2):
    r"""
    CDO operator: monsub
    """
    operator = CdoOperator(command="monsub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
