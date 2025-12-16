
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhouradd(self, ifile2):
    r"""
    CDO operator: yhouradd
    """
    operator = CdoOperator(command="yhouradd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
