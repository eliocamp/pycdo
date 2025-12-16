
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_cwdi(self, ifile2, optional):
    r"""
    CDO operator: eca_cwdi
Parameters:
    optional: ['INTEGER - Number of consecutive days (default: nday = 6)', 'FLOAT - Temperature offset (unit: °C; default: T = 5°C)']
    """
    operator = CdoOperator(command="eca_cwdi",
                           n_input=2, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
