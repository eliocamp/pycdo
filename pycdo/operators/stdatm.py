
from ..cdo_operator import CdoOperator
inf=float("inf")
def stdatm(self, optional):
    r"""
    CDO operator: stdatm
Parameters:
    optional: ['FLOAT - Constant', 'INTEGER - The seed for a new sequence of pseudo-random numbers \\[default: 1\\]', 'STRING - Target grid description file or name', 'FLOAT - Start value of the loop', 'FLOAT - End value of the loop', 'FLOAT - Increment of the loop \\[default: 1\\]', 'FLOAT - Target levels in metre above surface']
    """
    operator = CdoOperator(command="stdatm",
                           n_input=0, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
