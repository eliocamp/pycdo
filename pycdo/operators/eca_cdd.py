
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_cdd(self, optional):
    r"""
    CDO operator: eca_cdd
Parameters:
    optional: ['FLOAT - Precipitation threshold (unit: mm; default: R = 1 mm)', 'INTEGER - Minimum number of days exceeded (default: N = 5)', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="eca_cdd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
