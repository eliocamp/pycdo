
from ..cdo_operator import CdoOperator
inf=float("inf")
def splityear(self, optional):
    r"""
    CDO operator: splityear
Parameters:
    optional: STRING - C-style format for strftime() (e.g. %B for the full month name)
    """
    operator = CdoOperator(command="splityear",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
