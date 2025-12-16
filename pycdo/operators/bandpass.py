
from ..cdo_operator import CdoOperator
inf=float("inf")
def bandpass(self, optional):
    r"""
    CDO operator: bandpass
Parameters:
    optional: ['FLOAT\tMinimum - frequency per year that passes the filter.', 'FLOAT\tMaximum - frequency per year that passes the filter.']
    """
    operator = CdoOperator(command="bandpass",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
