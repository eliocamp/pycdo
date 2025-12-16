
from ..cdo_operator import CdoOperator
inf=float("inf")
def eofcoeff(self, ifile2):
    r"""
    CDO operator: eofcoeff
    """
    operator = CdoOperator(command="eofcoeff",
                           n_input=2, 
                           n_output=inf, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
