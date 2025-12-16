
from ..cdo_operator import CdoOperator
inf=float("inf")
def intlevel(self, optional):
    r"""
    CDO operator: intlevel
Parameters:
    optional: ['FLOAT - Comma-separated list of target levels', 'STRING - Path to a file containing a description of the Z-axis', 'STRING - Use zvarname as the vertical 3D source coordinate instead of the 1D coordinate variable', 'BOOL - Fill target layers out of the source layer range with the nearest source layer']
    """
    operator = CdoOperator(command="intlevel",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
