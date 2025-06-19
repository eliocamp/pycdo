
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapbil(self, grid):
    """
    CDO operator: remapbil
Parameters:
    grid: grid to remap to
    """
    operator = CdoOperator(name="remapbil",
                           num_inputs=1, 
                           num_outputs=1, 
                           parameters=[grid])
    return self._new_op(operator, [], {"grid": grid})
