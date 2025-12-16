
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonlt(self, ifile2):
    r"""
    CDO operator: ymonlt
    """
    operator = CdoOperator(command="ymonlt",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
