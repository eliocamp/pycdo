
from ..cdo_operator import CdoOperator
inf=float("inf")
def collgrid(self, optional):
    r"""
    CDO operator: collgrid
Parameters:
    optional: ['INTEGER - Number of regions in x direction \\[default: number of input files\\]', 'STRING - Comma-separated list of variable names \\[default: all variables\\]']
    """
    operator = CdoOperator(command="collgrid",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
