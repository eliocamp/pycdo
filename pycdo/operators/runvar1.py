
from ..cdo_operator import CdoOperator
inf=float("inf")
def runvar1(self, optional):
    r"""
    CDO operator: runvar1
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runvar1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
