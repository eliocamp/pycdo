
from ..cdo_operator import CdoOperator
inf=float("inf")
def ne(self, ifile2):
    r"""
    CDO operator: ne
    """
    operator = CdoOperator(command="ne",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
