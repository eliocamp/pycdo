
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_rr1(self, optional):
    r"""
    CDO operator: eca_rr1
Parameters:
    optional: FLOAT - Precipitation threshold (unit: mm; default: R = 1 mm)
    """
    operator = CdoOperator(command="eca_rr1",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
