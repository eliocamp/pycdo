
from cdo_operator import CdoOperator
inf=float("inf")
def remapbil(self, grid):
    """
     
    """
    operator = CdoOperator(name="remapbil",
                           num_inputs=1, 
                           num_outputs=1, 
                           parameters=[grid])
    return self._new_op(operator, [], {"grid": grid})
