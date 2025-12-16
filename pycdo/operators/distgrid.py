
from ..cdo_operator import CdoOperator
inf=float("inf")
def distgrid(self, optional):
    r"""
    CDO operator: distgrid
Parameters:
    optional: ['INTEGER - Number of regions in x direction, or number of pieces for unstructured grids', 'INTEGER - Number of regions in y direction \\[default: 1\\]']
    """
    operator = CdoOperator(command="distgrid",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
