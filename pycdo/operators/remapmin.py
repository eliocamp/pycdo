
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapmin(self, optional):
    r"""
    CDO operator: remapmin
Parameters:
    optional: STRING - Target grid description file or name
    """
    operator = CdoOperator(command="remapmin",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
