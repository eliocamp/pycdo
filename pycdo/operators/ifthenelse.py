
from ..cdo_operator import CdoOperator
inf=float("inf")
def ifthenelse(self, ifile2, ifile3):
    r"""
    CDO operator: ifthenelse
    """
    operator = CdoOperator(command="ifthenelse",
                           n_input=3, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2, ifile3], {})
