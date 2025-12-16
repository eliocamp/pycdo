
from ..cdo_operator import CdoOperator
inf=float("inf")
def input(self, optional):
    r"""
    CDO operator: input
Parameters:
    optional: ['STRING - Grid description file or name', 'STRING - Z-axis description file']
    """
    operator = CdoOperator(command="input",
                           n_input=0, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
