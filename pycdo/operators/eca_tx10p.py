
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_tx10p(self, ifile2):
    r"""
    CDO operator: eca_tx10p
    """
    operator = CdoOperator(command="eca_tx10p",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
