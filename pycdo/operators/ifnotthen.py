
from ..cdo_operator import CdoOperator
inf=float("inf")
def ifnotthen(self, ifile2):
    r"""
    CDO operator: ifnotthen
    """
    operator = CdoOperator(command="ifnotthen",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
