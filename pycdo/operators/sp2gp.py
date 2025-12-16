
from ..cdo_operator import CdoOperator
inf=float("inf")
def sp2gp(self, optional):
    r"""
    CDO operator: sp2gp
Parameters:
    optional: ['STRING - Type of the grid: quadratic, linear, cubic (default: type=quadratic)', 'STRING - Triangular truncation']
    """
    operator = CdoOperator(command="sp2gp",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
