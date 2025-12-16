
from ..cdo_operator import CdoOperator
inf=float("inf")
def seltimeidx(self, ifile2):
    r"""
    CDO operator: seltimeidx
    """
    operator = CdoOperator(command="seltimeidx",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
