
from ..cdo_operator import CdoOperator
inf=float("inf")
def daydiv(self, ifile2):
    r"""
    CDO operator: daydiv
    """
    operator = CdoOperator(command="daydiv",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
