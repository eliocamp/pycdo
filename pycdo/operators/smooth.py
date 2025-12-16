
from ..cdo_operator import CdoOperator
inf=float("inf")
def smooth(self, optional):
    r"""
    CDO operator: smooth
Parameters:
    optional: ['INTEGER - Number of times to smooth, default nsmooth=1', 'STRING - Search radius, default radius=1deg (units: deg, rad, km, m)', 'INTEGER - Maximum number of points, default maxpoints=<gridsize>', 'STRING - Weighting method, default weighted=linear', 'FLOAT - Weight at distance 0, default weight0=0.25', 'FLOAT - Weight at the search radius, default weightR=0.25']
    """
    operator = CdoOperator(command="smooth",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
