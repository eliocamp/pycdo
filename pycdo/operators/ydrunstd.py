
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydrunstd(self, optional):
    r"""
    CDO operator: ydrunstd
Parameters:
    optional: ['INTEGER - Number of timesteps', 'STRING - Read method circular']
    """
    operator = CdoOperator(command="ydrunstd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
