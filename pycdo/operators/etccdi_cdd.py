
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_cdd(self, optional):
    r"""
    CDO operator: etccdi_cdd
Parameters:
    optional: ['FLOAT - Precipitation threshold (unit: mm; default: R = 1 mm)', 'INTEGER - Minimum number of days exceeded (default: N = 5)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="etccdi_cdd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
