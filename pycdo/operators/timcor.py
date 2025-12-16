
from ..cdo_operator import CdoOperator
inf=float("inf")
def timcor(self, ifile2):
    r"""
    CDO operator: timcor
    """
    operator = CdoOperator(command="timcor",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
