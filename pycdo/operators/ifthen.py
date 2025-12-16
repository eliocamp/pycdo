
from ..cdo_operator import CdoOperator
inf=float("inf")
def ifthen(self, ifile2):
    r"""
    CDO operator: ifthen
    """
    operator = CdoOperator(command="ifthen",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
