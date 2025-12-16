
from ..cdo_operator import CdoOperator
inf=float("inf")
def runsum(self, optional):
    r"""
    CDO operator: runsum
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runsum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
