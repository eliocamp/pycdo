
from ..cdo_operator import CdoOperator
inf=float("inf")
def ymongt(self, ifile2):
    r"""
    CDO operator: ymongt
    """
    operator = CdoOperator(command="ymongt",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
