
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydrunsum(self, optional):
    r"""
    CDO operator: ydrunsum
Parameters:
    optional: ['INTEGER - Number of timesteps', 'STRING - Read method circular']
    """
    operator = CdoOperator(command="ydrunsum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
