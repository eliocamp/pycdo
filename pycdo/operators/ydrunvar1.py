
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydrunvar1(self, optional):
    r"""
    CDO operator: ydrunvar1
Parameters:
    optional: ['INTEGER - Number of timesteps', 'STRING - Read method circular']
    """
    operator = CdoOperator(command="ydrunvar1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
