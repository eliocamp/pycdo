
from ..cdo_operator import CdoOperator
inf=float("inf")
def ge(self, ifile2):
    r"""
    CDO operator: ge
    """
    operator = CdoOperator(command="ge",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
