
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapavg(self, optional):
    r"""
    CDO operator: remapavg
Parameters:
    optional: STRING - Target grid description file or name
    """
    operator = CdoOperator(command="remapavg",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
