
from ..cdo_operator import CdoOperator
inf=float("inf")
def sp2sp(self, optional):
    r"""
    CDO operator: sp2sp
Parameters:
    optional: INTEGER - New spectral resolution
    """
    operator = CdoOperator(command="sp2sp",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
