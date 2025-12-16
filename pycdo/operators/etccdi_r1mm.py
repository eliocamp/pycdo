
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_r1mm(self, optional):
    r"""
    CDO operator: etccdi_r1mm
Parameters:
    optional: ['FLOAT - Daily precipitation amount threshold in \\[mm\\]', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="etccdi_r1mm",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
