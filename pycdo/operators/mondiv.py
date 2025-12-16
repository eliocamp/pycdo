
from ..cdo_operator import CdoOperator
inf=float("inf")
def mondiv(self, ifile2):
    r"""
    CDO operator: mondiv
    """
    operator = CdoOperator(command="mondiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
