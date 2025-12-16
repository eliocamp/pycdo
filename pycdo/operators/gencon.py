
from ..cdo_operator import CdoOperator
inf=float("inf")
def gencon(self, optional):
    r"""
    CDO operator: gencon
Parameters:
    optional: ['STRING - Target grid description file or name', 'BOOL - Generate all mapfiles of the first 3D field']
    """
    operator = CdoOperator(command="gencon",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
