
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_tr(self, optional):
    r"""
    CDO operator: etccdi_tr
Parameters:
    optional: ['FLOAT - Temperature threshold (unit: °C; default: T = 20°C)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="etccdi_tr",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
