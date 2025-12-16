
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydrunstd1(self, optional):
    r"""
    CDO operator: ydrunstd1
Parameters:
    optional: ['INTEGER - Number of timesteps', 'STRING - Read method circular']
    """
    operator = CdoOperator(command="ydrunstd1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
