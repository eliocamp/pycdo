
from ..cdo_operator import CdoOperator
inf=float("inf")
def setpartabn(self, optional):
    r"""
    CDO operator: setpartabn
Parameters:
    optional: ['STRING - Parameter table file or name', 'STRING - Converts the units if necessary']
    """
    operator = CdoOperator(command="setpartabn",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
