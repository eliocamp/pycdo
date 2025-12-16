
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_r99ptot(self, ifile2):
    r"""
    CDO operator: eca_r99ptot
    """
    operator = CdoOperator(command="eca_r99ptot",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
