
from ..cdo_operator import CdoOperator
inf=float("inf")
def settime(self, optional):
    r"""
    CDO operator: settime
Parameters:
    optional: ['INTEGER - Value of the new day', 'INTEGER - Value of the new month', 'INTEGER - Value of the new year', 'STRING - Base units of the time axis (seconds|minutes|hours|days|months|years)', 'STRING - Date (format: YYYY-MM-DD)', 'STRING - Time (format: hh:mm:ss)', 'STRING - Optional increment (seconds|minutes|hours|days|months|years) \\[default: 1hour\\]', 'STRING - Frequency of the time series (hour|day|month|year)', 'STRING - Calendar (standard|proleptic_gregorian|360_day|365_day|366_day)', 'STRING - Shift value (e.g. -3hour)']
    """
    operator = CdoOperator(command="settime",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
