
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_r20mm(self, optional):
    r"""
    CDO operator: eca_r20mm
Parameters:
    optional: ['FLOAT - Daily precipitation amount threshold in \\[mm\\]', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="eca_r20mm",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
