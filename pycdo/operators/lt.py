
from ..cdo_operator import CdoOperator
inf=float("inf")
def lt(self, ifile2):
    r"""
    CDO operator: lt
    """
    operator = CdoOperator(command="lt",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
