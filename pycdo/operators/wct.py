
from ..cdo_operator import CdoOperator
inf=float("inf")
def wct(self, ifile2):
    r"""
    CDO operator: wct
    """
    operator = CdoOperator(command="wct",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
