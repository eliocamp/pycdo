
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_sdii(self, optional):
    r"""
    CDO operator: eca_sdii
Parameters:
    optional: FLOAT - Precipitation threshold (unit: mm; default: R = 1 mm)
    """
    operator = CdoOperator(command="eca_sdii",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
