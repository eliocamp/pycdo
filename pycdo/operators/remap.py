
from ..cdo_operator import CdoOperator
inf=float("inf")
def remap(self, optional):
    r"""
    CDO operator: remap
Parameters:
    optional: ['STRING - Target grid description file or name', 'STRING - Interpolation weights (SCRIP NetCDF file)']
    """
    operator = CdoOperator(command="remap",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
