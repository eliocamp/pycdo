
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_etr(self, ifile2):
    r"""
    CDO operator: eca_etr
    """
    operator = CdoOperator(command="eca_etr",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
