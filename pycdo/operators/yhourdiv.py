
from ..cdo_operator import CdoOperator
inf=float("inf")
def yhourdiv(self, ifile2):
    r"""
    CDO operator: yhourdiv
    """
    operator = CdoOperator(command="yhourdiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
