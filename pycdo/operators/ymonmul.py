
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonmul(self, ifile2):
    r"""
    CDO operator: ymonmul
    """
    operator = CdoOperator(command="ymonmul",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
