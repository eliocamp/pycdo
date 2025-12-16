
from ..cdo_operator import CdoOperator
inf=float("inf")
def timselstd(self, optional):
    r"""
    CDO operator: timselstd
Parameters:
    optional: ['INTEGER - Number of input timesteps for each output timestep', 'INTEGER - Number of input timesteps skipped before the first timestep range (optional)', 'INTEGER - Number of input timesteps skipped between timestep ranges (optional)']
    """
    operator = CdoOperator(command="timselstd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
