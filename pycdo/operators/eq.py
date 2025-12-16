
from ..cdo_operator import CdoOperator
inf=float("inf")
def eq(self, ifile2):
    r"""
    CDO operator: eq
    """
    operator = CdoOperator(command="eq",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
