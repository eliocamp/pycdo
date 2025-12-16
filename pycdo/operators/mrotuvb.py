
from ..cdo_operator import CdoOperator
inf=float("inf")
def mrotuvb(self, ifile2):
    r"""
    CDO operator: mrotuvb
    """
    operator = CdoOperator(command="mrotuvb",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
