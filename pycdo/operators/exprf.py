
from ..cdo_operator import CdoOperator
inf=float("inf")
def exprf(self, optional):
    r"""
    CDO operator: exprf
Parameters:
    optional: ["STRING - Processing instructions (need to be 'quoted' in most cases)", 'STRING - File with processing instructions']
    """
    operator = CdoOperator(command="exprf",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
