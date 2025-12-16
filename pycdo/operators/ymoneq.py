
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymoneq(self, ifile2):
    r"""
    CDO operator: ymoneq
    """
    operator = CdoOperator(command="ymoneq",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
