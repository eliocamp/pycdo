
from ..cdo_operator import CdoOperator
inf=float("inf")
def intlevelx3d(self, ifile2, optional):
    r"""
    CDO operator: intlevelx3d
Parameters:
    optional: STRING - filename for 3D vertical target coordinates
    """
    operator = CdoOperator(command="intlevelx3d",
                           n_input=2, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
