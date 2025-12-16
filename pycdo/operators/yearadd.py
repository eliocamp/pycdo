
from ..cdo_operator import CdoOperator
inf=float("inf")
def yearadd(self, ifile2):
    r"""
    CDO operator: yearadd
    """
    operator = CdoOperator(command="yearadd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
