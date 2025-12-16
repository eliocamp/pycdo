
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_fd(self, optional):
    r"""
    CDO operator: etccdi_fd
Parameters:
    optional: STRING - Output frequency (year, month)
    """
    operator = CdoOperator(command="etccdi_fd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
