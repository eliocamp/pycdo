
from ..cdo_operator import CdoOperator
inf=float("inf")
def aexpr(self, optional):
    r"""
    CDO operator: aexpr
Parameters:
    optional: ["STRING - Processing instructions (need to be 'quoted' in most cases)", 'STRING - File with processing instructions']
    """
    operator = CdoOperator(command="aexpr",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
