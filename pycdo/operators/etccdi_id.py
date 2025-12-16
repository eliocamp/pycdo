
from ..cdo_operator import CdoOperator
inf=float("inf")
def etccdi_id(self, optional):
    r"""
    CDO operator: etccdi_id
Parameters:
    optional: STRING - Output frequency (year, month)
    """
    operator = CdoOperator(command="etccdi_id",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
