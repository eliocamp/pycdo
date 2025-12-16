
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_csu(self, optional):
    r"""
    CDO operator: eca_csu
Parameters:
    optional: ['FLOAT - Temperature threshold (unit: °C; default: T = 25°C)', 'INTEGER - Minimum number of days exceeded (default: N = 5)']
    """
    operator = CdoOperator(command="eca_csu",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
