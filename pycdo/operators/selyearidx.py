
from ..cdo_operator import CdoOperator
inf=float("inf")
def selyearidx(self, ifile2):
    r"""
    CDO operator: selyearidx
    """
    operator = CdoOperator(command="selyearidx",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
