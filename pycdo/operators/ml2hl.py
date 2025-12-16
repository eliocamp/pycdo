
from ..cdo_operator import CdoOperator
inf=float("inf")
def ml2hl(self, optional):
    r"""
    CDO operator: ml2hl
Parameters:
    optional: ['FLOAT - Pressure levels in pascal', 'FLOAT - Height levels in meter']
    """
    operator = CdoOperator(command="ml2hl",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
