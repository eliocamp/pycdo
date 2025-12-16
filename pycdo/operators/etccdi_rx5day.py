
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_rx5day(self, optional):
    r"""
    CDO operator: etccdi_rx5day
Parameters:
    optional: ['FLOAT - Precipitation threshold (unit: mm; default: x = 50 mm)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="etccdi_rx5day",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
