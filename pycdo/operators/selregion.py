
from ..cdo_operator import CdoOperator
inf=float("inf")
def selregion(self, optional):
    r"""
    CDO operator: selregion
Parameters:
    optional: ['STRING - Comma-separated list of ASCII formatted files with different regions', 'FLOAT - Longitude of the center of the circle in degrees, default lon=0.0', 'FLOAT - Latitude of the center of the circle in degrees, default lat=0.0', 'STRING - Radius of the circle, default radius=1deg (units: deg, rad, km, m)']
    """
    operator = CdoOperator(command="selregion",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
