
from ..cdo_operator import CdoOperator
inf=float("inf")
def fourier(self, optional):
    r"""
    CDO operator: fourier
Parameters:
    optional: INTEGER - -1: forward transformation; 1: backward transformation
    """
    operator = CdoOperator(command="fourier",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
