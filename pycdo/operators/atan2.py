
from ..cdo_operator import CdoOperator
inf=float("inf")
def atan2(self, ifile2):
    r"""
    CDO operator: atan2
    """
    operator = CdoOperator(command="atan2",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
