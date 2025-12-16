
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonle(self, ifile2):
    r"""
    CDO operator: ymonle
    """
    operator = CdoOperator(command="ymonle",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
