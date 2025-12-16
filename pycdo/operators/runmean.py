
from ..cdo_operator import CdoOperator
inf=float("inf")
def runmean(self, optional):
    r"""
    CDO operator: runmean
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runmean",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
