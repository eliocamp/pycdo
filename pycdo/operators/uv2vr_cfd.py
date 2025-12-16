
from ..cdo_operator import CdoOperator
inf=float("inf")
def uv2vr_cfd(self, optional):
    r"""
    CDO operator: uv2vr_cfd
Parameters:
    optional: ['STRING - Name of variable u (default: u)', 'STRING - Name of variable v (default: v)', 'INTEGER - Boundary condition option (0-3) (default: 0/1 for cyclic grids)', 'STRING - Output mode new/append (default: new)']
    """
    operator = CdoOperator(command="uv2vr_cfd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
