
from ..cdo_operator import CdoOperator
inf=float("inf")
def splitmon(self, optional):
    r"""
    CDO operator: splitmon
Parameters:
    optional: STRING - C-style format for strftime() (e.g. %B for the full month name)
    """
    operator = CdoOperator(command="splitmon",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
