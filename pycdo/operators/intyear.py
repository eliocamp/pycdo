
from ..cdo_operator import CdoOperator
inf=float("inf")
def intyear(self, ifile2, optional):
    r"""
    CDO operator: intyear
Parameters:
    optional: INTEGER - Comma-separated list or first/last\[/inc\] range of years
    """
    operator = CdoOperator(command="intyear",
                           n_input=2, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
