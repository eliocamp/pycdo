
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapbic(self, optional):
    r"""
    CDO operator: remapbic
Parameters:
    optional: ['STRING - Target grid description file or name', 'BOOL - Generate all mapfiles of the first 3D field']
    """
    operator = CdoOperator(command="remapbic",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
