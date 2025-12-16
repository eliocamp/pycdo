
from ..cdo_operator import CdoOperator
inf=float("inf")
def dayadd(self, ifile2):
    r"""
    CDO operator: dayadd
    """
    operator = CdoOperator(command="dayadd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
