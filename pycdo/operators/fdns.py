
from ..cdo_operator import CdoOperator
inf=float("inf")
def fdns(self, ifile2):
    r"""
    CDO operator: fdns
    """
    operator = CdoOperator(command="fdns",
                           n_input=2, 
                           n_output=1, 
                           params=[])
    return self._new_op(operator, [ifile2], {})
