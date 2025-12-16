
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapeta(self, optional):
    r"""
    CDO operator: remapeta
Parameters:
    optional: ['STRING - File name of an ASCII dataset with the vertical coordinate table', 'STRING - File name with the orography (surf. geopotential) of the target dataset (optional)']
    """
    operator = CdoOperator(command="remapeta",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
