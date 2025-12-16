
from ..cdo_operator import CdoOperator
inf=float("inf")
def yseassub(self, ifile2):
    r"""
    CDO operator: yseassub
    """
    operator = CdoOperator(command="yseassub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
