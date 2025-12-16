
from ..cdo_operator import CdoOperator
inf=float("inf")
def eofspatial(self, optional):
    r"""
    CDO operator: eofspatial
Parameters:
    optional: INTEGER - Number of eigen functions
    """
    operator = CdoOperator(command="eofspatial",
                           n_input=1, 
                           n_output=2, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
