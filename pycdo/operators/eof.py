
from ..cdo_operator import CdoOperator
inf=float("inf")
def eof(self, optional):
    r"""
    CDO operator: eof
Parameters:
    optional: INTEGER - Number of eigen functions
    """
    operator = CdoOperator(command="eof",
                           n_input=1, 
                           n_output=2, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
