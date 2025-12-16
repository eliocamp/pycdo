
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_rx5day(self, optional):
    r"""
    CDO operator: eca_rx5day
Parameters:
    optional: ['FLOAT - Precipitation threshold (unit: mm; default: x = 50 mm)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="eca_rx5day",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
