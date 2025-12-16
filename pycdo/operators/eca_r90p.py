
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_r90p(self, ifile2):
    r"""
    CDO operator: eca_r90p
    """
    operator = CdoOperator(command="eca_r90p",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
