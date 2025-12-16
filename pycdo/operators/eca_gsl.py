
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_gsl(self, ifile2, optional):
    r"""
    CDO operator: eca_gsl
Parameters:
    optional: ['INTEGER - Number of consecutive days (default: nday = 6)', 'FLOAT - Temperature threshold (unit: °C; default: T = 5°C)', 'FLOAT - Land fraction threshold (default: fland = 0.5)']
    """
    operator = CdoOperator(command="eca_gsl",
                           n_input=2, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
