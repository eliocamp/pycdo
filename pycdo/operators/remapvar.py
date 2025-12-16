
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapvar(self, optional):
    r"""
    CDO operator: remapvar
Parameters:
    optional: STRING - Target grid description file or name
    """
    operator = CdoOperator(command="remapvar",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
