
from ..cdo_operator import CdoOperator
inf=float("inf")
def intntime(self, optional):
    r"""
    CDO operator: intntime
Parameters:
    optional: ['STRING - Start date (format YYYY-MM-DD)', 'STRING - Start time (format hh:mm:ss)', 'STRING - Optional increment (seconds, minutes, hours, days, months, years) \\[default: 0hour\\]', 'INTEGER - Number of timesteps from one timestep to the next']
    """
    operator = CdoOperator(command="intntime",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
