
from ..cdo_operator import CdoOperator
inf=float("inf")
def gh2hl(self, optional):
    r"""
    CDO operator: gh2hl
Parameters:
    optional: FLOAT - Comma-separated list of height levels in meter
    """
    operator = CdoOperator(command="gh2hl",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
