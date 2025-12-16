
from ..cdo_operator import CdoOperator
inf=float("inf")
def add(self, ifile2):
    r"""
    CDO operator: add
    """
    operator = CdoOperator(command="add",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
