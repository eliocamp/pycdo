
from ..cdo_operator import CdoOperator
inf=float("inf")
def timcovar(self, ifile2):
    r"""
    CDO operator: timcovar
    """
    operator = CdoOperator(command="timcovar",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
