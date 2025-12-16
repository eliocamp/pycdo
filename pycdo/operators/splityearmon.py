
from ..cdo_operator import CdoOperator
inf=float("inf")
def splityearmon(self, optional):
    r"""
    CDO operator: splityearmon
Parameters:
    optional: STRING - C-style format for strftime() (e.g. %B for the full month name)
    """
    operator = CdoOperator(command="splityearmon",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
