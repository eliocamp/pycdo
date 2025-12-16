
from ..cdo_operator import CdoOperator
inf=float("inf")
def eof3d(self, optional):
    r"""
    CDO operator: eof3d
Parameters:
    optional: INTEGER - Number of eigen functions
    """
    operator = CdoOperator(command="eof3d",
                           n_input=1, 
                           n_output=2, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
