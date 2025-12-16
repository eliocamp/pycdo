
from ..cdo_operator import CdoOperator
inf=float("inf")
def runpctl(self, optional):
    r"""
    CDO operator: runpctl
Parameters:
    optional: ['FLOAT - Percentile number in \\{0, ..., 100\\}', 'INTEGER - Number of timesteps']
    """
    operator = CdoOperator(command="runpctl",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
