
from ..cdo_operator import CdoOperator
inf=float("inf")
def runstd1(self, optional):
    r"""
    CDO operator: runstd1
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runstd1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
