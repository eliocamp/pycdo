
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_su(self, optional):
    r"""
    CDO operator: eca_su
Parameters:
    optional: ['FLOAT - Temperature threshold (unit: °C; default: T = 25°C)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="eca_su",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
