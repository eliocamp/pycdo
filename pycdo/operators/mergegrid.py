
from ..cdo_operator import CdoOperator
inf=float("inf")
def mergegrid(self, ifile2):
    r"""
    CDO operator: mergegrid
    """
    operator = CdoOperator(command="mergegrid",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
