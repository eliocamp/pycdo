
from ..cdo_operator import CdoOperator
inf=float("inf")
def intlevel3d(self, ifile2, optional):
    r"""
    CDO operator: intlevel3d
Parameters:
    optional: STRING - filename for 3D vertical target coordinates
    """
    operator = CdoOperator(command="intlevel3d",
                           n_input=2, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2], {"optional": optional})
