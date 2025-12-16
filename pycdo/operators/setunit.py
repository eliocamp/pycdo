
from ..cdo_operator import CdoOperator
inf=float("inf")
def setunit(self, optional):
    r"""
    CDO operator: setunit
Parameters:
    optional: ['STRING - Parameter table file or name', 'INTEGER - Code number', 'STRING - Parameter identifier (GRIB1: code\\[.tabnum\\]; GRIB2: num\\[.cat\\[.dis\\]\\])', 'STRING - Variable name', 'FLOAT - New level', 'INTEGER - GRIB level type', 'INTEGER - Maximum number of timesteps']
    """
    operator = CdoOperator(command="setunit",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
