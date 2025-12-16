
from ..cdo_operator import CdoOperator
inf=float("inf")
def reducegrid(self, optional):
    r"""
    CDO operator: reducegrid
Parameters:
    optional: ['STRING - file which holds the mask field', "STRING - optional parameter to limit coordinates output: 'nobounds' disables coordinate bounds, 'nocoords' avoids all coordinate information"]
    """
    operator = CdoOperator(command="reducegrid",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
