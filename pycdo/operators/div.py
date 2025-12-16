
from ..cdo_operator import CdoOperator
inf=float("inf")
def div(self, ifile2):
    r"""
    CDO operator: div
    """
    operator = CdoOperator(command="div",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
