
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_hd(self, optional):
    r"""
    CDO operator: eca_hd
Parameters:
    optional: ['FLOAT - Temperature limit (unit: °C; default: T1 = 17°C)', 'FLOAT - Temperature limit (unit: °C; default: T2 = T1)']
    """
    operator = CdoOperator(command="eca_hd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
