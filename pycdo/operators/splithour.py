
from ..cdo_operator import CdoOperator
inf=float("inf")
def splithour(self, optional):
    r"""
    CDO operator: splithour
Parameters:
    optional: STRING - C-style format for strftime() (e.g. %B for the full month name)
    """
    operator = CdoOperator(command="splithour",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
