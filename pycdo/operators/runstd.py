
from ..cdo_operator import CdoOperator
inf=float("inf")
def runstd(self, optional):
    r"""
    CDO operator: runstd
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runstd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
