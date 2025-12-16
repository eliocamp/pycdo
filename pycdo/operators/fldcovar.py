
from ..cdo_operator import CdoOperator
inf=float("inf")
def fldcovar(self, ifile2):
    r"""
    CDO operator: fldcovar
    """
    operator = CdoOperator(command="fldcovar",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
