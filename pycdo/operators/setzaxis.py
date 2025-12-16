
from ..cdo_operator import CdoOperator
inf=float("inf")
def setzaxis(self, optional):
    r"""
    CDO operator: setzaxis
Parameters:
    optional: ['STRING - Z-axis description file or name of the target z-axis', 'FLOAT - Specifying the bottom of the vertical column. Must have the same units as z-axis.', 'FLOAT - Specifying the top of the vertical column. Must have the same units as z-axis.']
    """
    operator = CdoOperator(command="setzaxis",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
