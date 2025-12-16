
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymondiv(self, ifile2):
    r"""
    CDO operator: ymondiv
    """
    operator = CdoOperator(command="ymondiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
