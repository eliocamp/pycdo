
from ..cdo_operator import CdoOperator
inf=float("inf")
def samplegrid(self, optional):
    r"""
    CDO operator: samplegrid
Parameters:
    optional: INTEGER - Resample factor, typically 2, which will half the resolution
    """
    operator = CdoOperator(command="samplegrid",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
