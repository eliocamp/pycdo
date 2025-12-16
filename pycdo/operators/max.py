
from ..cdo_operator import CdoOperator
inf=float("inf")
def max(self, ifile2):
    r"""
    CDO operator: max
    """
    operator = CdoOperator(command="max",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
