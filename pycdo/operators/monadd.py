
from ..cdo_operator import CdoOperator
inf=float("inf")
def monadd(self, ifile2):
    r"""
    CDO operator: monadd
    """
    operator = CdoOperator(command="monadd",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
