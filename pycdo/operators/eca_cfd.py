
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_cfd(self, optional):
    r"""
    CDO operator: eca_cfd
Parameters:
    optional: INTEGER - Minimum number of days exceeded (default: N = 5)
    """
    operator = CdoOperator(command="eca_cfd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
