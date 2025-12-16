
from ..cdo_operator import CdoOperator
inf=float("inf")
def min(self, ifile2):
    r"""
    CDO operator: min
    """
    operator = CdoOperator(command="min",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
