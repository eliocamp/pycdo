
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonadd(self, ifile2):
    r"""
    CDO operator: ymonadd
    """
    operator = CdoOperator(command="ymonadd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
