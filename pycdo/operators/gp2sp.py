
from ..cdo_operator import CdoOperator
inf=float("inf")
def gp2sp(self, optional):
    r"""
    CDO operator: gp2sp
Parameters:
    optional: ['STRING - Type of the grid: quadratic, linear, cubic (default: type=quadratic)', 'STRING - Triangular truncation']
    """
    operator = CdoOperator(command="gp2sp",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
