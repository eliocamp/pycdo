
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_r75p(self, ifile2):
    r"""
    CDO operator: eca_r75p
    """
    operator = CdoOperator(command="eca_r75p",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
