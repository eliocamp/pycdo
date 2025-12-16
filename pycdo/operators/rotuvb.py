
from ..cdo_operator import CdoOperator
inf=float("inf")
def rotuvb(self, optional):
    r"""
    CDO operator: rotuvb
Parameters:
    optional: ['STRING - Pairs of zonal and meridional velocity components (use variable names or code numbers)', 'STRING - Pairs of zonal and meridional velocity components (use variable names or code numbers)']
    """
    operator = CdoOperator(command="rotuvb",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
