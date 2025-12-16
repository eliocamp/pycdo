
from ..cdo_operator import CdoOperator
inf=float("inf")
def maskregion(self, optional):
    r"""
    CDO operator: maskregion
Parameters:
    optional: STRING - Comma-separated list of ASCII formatted files with different regions
    """
    operator = CdoOperator(command="maskregion",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
