
from ..cdo_operator import CdoOperator
inf=float("inf")
def grfill(self, optional):
    r"""
    CDO operator: grfill
Parameters:
    optional: STRING - Comma-separated list of plot parameters
    """
    operator = CdoOperator(command="grfill",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
