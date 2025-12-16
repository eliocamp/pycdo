
from ..cdo_operator import CdoOperator
inf=float("inf")
def selgrid(self, optional):
    r"""
    CDO operator: selgrid
Parameters:
    optional: ['STRING - Comma-separated list of parameter identifiers.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of code numbers.', 'STRING - Comma-separated list of variable names.', 'STRING - Comma-separated list of standard names.', 'FLOAT - Comma-separated list of vertical levels.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of index of levels.', 'INTEGER - Comma-separated list or first/last\\[/inc\\] range of GRIB level types.', 'STRING - Comma-separated list of grid names or numbers.', 'STRING - Comma-separated list of z-axis types or numbers.', 'STRING - Comma-separated list of z-axis names.', 'INTEGER - Comma-separated list or range of parameter table numbers.']
    """
    operator = CdoOperator(command="selgrid",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
