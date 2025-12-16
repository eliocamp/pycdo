
from ..cdo_operator import CdoOperator
inf=float("inf")
def select(self, optional):
    r"""
    CDO operator: select
Parameters:
    optional: ['STRING - Comma-separated list of variable names.', 'STRING - Comma-separated list of parameter identifiers.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of code numbers.', 'FLOAT - Comma-separated list of vertical levels.', 'FLOAT - First and last value of the level range.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of index of levels.', 'STRING - Comma-separated list of zaxis names.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of zaxis numbers.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of GRIB level types.', 'STRING - Comma-separated list of grid names.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of grid numbers.', 'STRING - Comma-separated list of timestep types (constant|avg|accum|min|max|range|diff|sum)', 'STRING - Comma-separated list of dates (format: YYYY-MM-DDThh:mm:ss).', 'STRING - Start date (format: YYYY-MM-DDThh:mm:ss).', 'STRING - End date (format: YYYY-MM-DDThh:mm:ss).', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of minutes.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of hours.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of days.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of months.', 'STRING - Comma-separated list of seasons (substring of DJFMAMJJASOND or ANN).', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of years.', 'STRING - Comma-separated list of the day of month (e.g. 29feb).', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of timesteps. Negative values select timesteps from the end (NetCDF only).', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of timesteps of year.', 'STRING - Read timesteps from a mask file.']
    """
    operator = CdoOperator(command="select",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
