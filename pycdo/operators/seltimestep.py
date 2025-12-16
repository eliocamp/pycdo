
from ..cdo_operator import CdoOperator
inf=float("inf")
def seltimestep(self, optional):
    r"""
    CDO operator: seltimestep
Parameters:
    optional: ['INTEGER - Comma-separated list or first/last\\[/inc\\] range of timesteps. Negative values select timesteps from the end (NetCDF only).', 'STRING - Comma-separated list of times (format hh:mm:ss).', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of hours.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of days.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of months.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of years.', 'STRING - Comma-separated list of seasons (substring of DJFMAMJJASOND or ANN).', 'STRING - Start date (format: YYYY-MM-DDThh:mm:ss).', 'STRING - End date (format: YYYY-MM-DDThh:mm:ss) \\[default: startdate\\].', 'INTEGER - Number of timesteps before the selected month \\[default: 0\\].', 'INTEGER - Number of timesteps after the selected month \\[default: nts1\\].']
    """
    operator = CdoOperator(command="seltimestep",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
