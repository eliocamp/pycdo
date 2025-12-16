
from ..cdo_operator import CdoOperator
inf=float("inf")
def fldstd(self, optional):
    r"""
    CDO operator: fldstd
Parameters:
    optional: ['BOOL - weights=FALSE disables weighting by grid cell area \\[default: weights=TRUE\\]', 'FLOAT - Percentile number in \\{0, ..., 100\\}']
    """
    operator = CdoOperator(command="fldstd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
