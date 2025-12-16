
from ..cdo_operator import CdoOperator
inf=float("inf")
def splitsel(self, optional):
    r"""
    CDO operator: splitsel
Parameters:
    optional: ['INTEGER - Number of input timesteps for each output file', 'INTEGER - Number of input timesteps skipped before the first timestep range (optional)', 'INTEGER - Number of input timesteps skipped between timestep ranges (optional)']
    """
    operator = CdoOperator(command="splitsel",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
