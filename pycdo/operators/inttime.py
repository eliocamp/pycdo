
from ..cdo_operator import CdoOperator
inf=float("inf")
def inttime(self, optional):
    r"""
    CDO operator: inttime
Parameters:
    optional: ['STRING - Start date (format YYYY-MM-DD)', 'STRING - Start time (format hh:mm:ss)', 'STRING - Optional increment (seconds, minutes, hours, days, months, years) \\[default: 0hour\\]', 'INTEGER - Number of timesteps from one timestep to the next']
    """
    operator = CdoOperator(command="inttime",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
