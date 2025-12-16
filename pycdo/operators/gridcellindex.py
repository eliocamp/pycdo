
from ..cdo_operator import CdoOperator
inf=float("inf")
def gridcellindex(self, optional):
    r"""
    CDO operator: gridcellindex
Parameters:
    optional: ['INTEGER - Longitude of the grid cell in degree', 'INTEGER - Latitude of the grid cell in degree']
    """
    operator = CdoOperator(command="gridcellindex",
                           n_input=1, 
                           n_output=0, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
