
from ..cdo_operator import CdoOperator
inf=float("inf")
def diffn(self, ifile2, optional):
    r"""
    CDO operator: diffn
Parameters:
    optional: ['INTEGER - Stop after maxcount different fields', 'FLOAT - Limit of the maximum absolute difference (default: 0)', 'FLOAT - Limit of the maximum relative difference (default: 1)', 'STRING - Consideration of the variable names of only one input file (left/right) or the intersection of both (intersect).']
    """
    operator = CdoOperator(command="diffn",
                           n_input=2, 
                           n_output=0, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
