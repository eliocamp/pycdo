
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_hwfi(self, ifile2, optional):
    r"""
    CDO operator: eca_hwfi
Parameters:
    optional: ['INTEGER - Number of consecutive days (default: nday = 6)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="eca_hwfi",
                           n_input=2, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
