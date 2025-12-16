
from ..cdo_operator import CdoOperator
inf=float("inf")
def outputint(self, optional):
    r"""
    CDO operator: outputint
Parameters:
    optional: ['STRING - C-style format for one element (e.g. %13.6g)', 'INTEGER - Number of elements for each row (default: nelem = 1)']
    """
    operator = CdoOperator(command="outputint",
                           n_input=inf, 
                           n_output=0, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
