
from ..cdo_operator import CdoOperator
inf=float("inf")
def fldvar(self, optional):
    r"""
    CDO operator: fldvar
Parameters:
    optional: ['BOOL - weights=FALSE disables weighting by grid cell area \\[default: weights=TRUE\\]', 'FLOAT - Percentile number in \\{0, ..., 100\\}']
    """
    operator = CdoOperator(command="fldvar",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
