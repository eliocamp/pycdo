
from ..cdo_operator import CdoOperator
inf=float("inf")
def timselpctl(self, ifile2, ifile3, optional):
    r"""
    CDO operator: timselpctl
Parameters:
    optional: ['FLOAT - Percentile number in \\{0, ..., 100\\}', 'INTEGER - Number of input timesteps for each output timestep', 'INTEGER - Number of input timesteps skipped before the first timestep range (optional)', 'INTEGER - Number of input timesteps skipped between timestep ranges (optional)']
    """
    operator = CdoOperator(command="timselpctl",
                           n_input=3, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2, ifile3], {"optional": optional})
