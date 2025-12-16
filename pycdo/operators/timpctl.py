
from ..cdo_operator import CdoOperator
inf=float("inf")
def timpctl(self, ifile2, ifile3, optional):
    r"""
    CDO operator: timpctl
Parameters:
    optional: FLOAT - Percentile number in \{0, ..., 100\}
    """
    operator = CdoOperator(command="timpctl",
                           n_input=3, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [ifile2, ifile3], {"optional": optional})
