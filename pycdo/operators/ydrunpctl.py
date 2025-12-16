
from ..cdo_operator import CdoOperator
inf=float("inf")
def ydrunpctl(self, ifile2, ifile3, optional):
    r"""
    CDO operator: ydrunpctl
Parameters:
    optional: ['FLOAT - Percentile number in \\{0, ..., 100\\}', 'INTEGER - Number of timesteps', 'STRING - Read method circular', 'STRING - Percentile method rtype8']
    """
    operator = CdoOperator(command="ydrunpctl",
                           n_input=3, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2, ifile3], {"optional": optional})
