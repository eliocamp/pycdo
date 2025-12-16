
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_csdi(self, ifile2, optional):
    r"""
    CDO operator: etccdi_csdi
Parameters:
    optional: ['INTEGER - Number of consecutive days (default: nday = 6)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="etccdi_csdi",
                           n_input=2, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
