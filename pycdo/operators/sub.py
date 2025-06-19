
from ..cdo_operator import CdoOperator
inf=float("inf")
def sub(self, ifile2):
    """
    CDO operator: sub
    """
    operator = CdoOperator(name="sub",
                           num_inputs=2, 
                           num_outputs=1, 
                           parameters=[])
    return self._new_op(operator, [ifile2], {})
