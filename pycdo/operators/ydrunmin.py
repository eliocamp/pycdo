
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydrunmin(self, optional):
    r"""
    CDO operator: ydrunmin
Parameters:
    optional: ['INTEGER - Number of timesteps', 'STRING - Read method circular']
    """
    operator = CdoOperator(command="ydrunmin",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
