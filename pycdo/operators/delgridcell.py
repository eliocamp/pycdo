
from ..cdo_operator import CdoOperator
inf=float("inf")
def delgridcell(self, optional):
    r"""
    CDO operator: delgridcell
Parameters:
    optional: INTEGER - Comma-separated list or first/last\[/inc\] range of indices
    """
    operator = CdoOperator(command="delgridcell",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
