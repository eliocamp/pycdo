
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapsum(self, optional):
    r"""
    CDO operator: remapsum
Parameters:
    optional: STRING - Target grid description file or name
    """
    operator = CdoOperator(command="remapsum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
