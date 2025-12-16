
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhoursub(self, ifile2):
    r"""
    CDO operator: yhoursub
    """
    operator = CdoOperator(command="yhoursub",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
