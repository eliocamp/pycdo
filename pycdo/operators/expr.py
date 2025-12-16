
from ..cdo_operator import CdoOperator
inf=float("inf")
def expr(self, optional):
    r"""
    CDO operator: expr
Parameters:
    optional: ["STRING - Processing instructions (need to be 'quoted' in most cases)", 'STRING - File with processing instructions']
    """
    operator = CdoOperator(command="expr",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
