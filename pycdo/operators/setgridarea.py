
from ..cdo_operator import CdoOperator
inf=float("inf")
def setgridarea(self, optional):
    r"""
    CDO operator: setgridarea
Parameters:
    optional: ['STRING - Grid description file or name', 'STRING - Grid type (curvilinear, unstructured, regular, lonlat, projection or dereference)', 'STRING - Data file, the first field is used as grid cell area', 'STRING - Data file, the first field is used as grid mask', 'STRING - Proj library parameter (e.g.:+init=EPSG:3413)']
    """
    operator = CdoOperator(command="setgridarea",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
