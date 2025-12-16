
from ..cdo_operator import CdoOperator
inf=float("inf")
def runvar(self, optional):
    r"""
    CDO operator: runvar
Parameters:
    optional: INTEGER - Number of timesteps
    """
    operator = CdoOperator(command="runvar",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
