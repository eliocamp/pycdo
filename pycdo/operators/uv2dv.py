
from ..cdo_operator import CdoOperator
inf=float("inf")
def uv2dv(self, optional):
    r"""
    CDO operator: uv2dv
Parameters:
    optional: STRING - Type of the grid: quadratic, linear, cubic (default: quadratic)
    """
    operator = CdoOperator(command="uv2dv",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
