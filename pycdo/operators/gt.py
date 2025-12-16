
from ..cdo_operator import CdoOperator
inf=float("inf")
def gt(self, ifile2):
    r"""
    CDO operator: gt
    """
    operator = CdoOperator(command="gt",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
