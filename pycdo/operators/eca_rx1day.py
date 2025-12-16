
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_rx1day(self, optional):
    r"""
    CDO operator: eca_rx1day
Parameters:
    optional: STRING - Output frequency (year, month)
    """
    operator = CdoOperator(command="eca_rx1day",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
