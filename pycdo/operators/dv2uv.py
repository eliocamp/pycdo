
from ..cdo_operator import CdoOperator
inf=float("inf")
def dv2uv(self, optional):
    r"""
    CDO operator: dv2uv
Parameters:
    optional: STRING - Type of the grid: quadratic, linear, cubic (default: quadratic)
    """
    operator = CdoOperator(command="dv2uv",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
