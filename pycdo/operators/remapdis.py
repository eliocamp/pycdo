
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapdis(self, optional):
    r"""
    CDO operator: remapdis
Parameters:
    optional: ['STRING - Target grid description file or name', 'INTEGER - Number of nearest neighbors \\[default: 4\\]', 'BOOL - Generate all mapfiles of the first 3D field']
    """
    operator = CdoOperator(command="remapdis",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
