
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymonge(self, ifile2):
    r"""
    CDO operator: ymonge
    """
    operator = CdoOperator(command="ymonge",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
