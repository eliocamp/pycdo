
from ..cdo_operator import CdoOperator
inf=float("inf")
def fldsum(self, optional):
    r"""
    CDO operator: fldsum
Parameters:
    optional: ['BOOL - weights=FALSE disables weighting by grid cell area \\[default: weights=TRUE\\]', 'FLOAT - Percentile number in \\{0, ..., 100\\}']
    """
    operator = CdoOperator(command="fldsum",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
