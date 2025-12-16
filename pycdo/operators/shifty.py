
from ..cdo_operator import CdoOperator
inf=float("inf")
def shifty(self, optional):
    r"""
    CDO operator: shifty
Parameters:
    optional: ['INTEGER - Number of grid cells to shift (default: 1)', 'STRING - If set, cells are filled up cyclic (default: missing value)', 'STRING - If set, coordinates are also shifted']
    """
    operator = CdoOperator(command="shifty",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
