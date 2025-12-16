
from ..cdo_operator import CdoOperator
inf=float("inf")
def runmax(self, optional):
    r"""
    CDO operator: runmax
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runmax",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
