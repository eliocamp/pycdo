
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_fd(self, optional):
    r"""
    CDO operator: eca_fd
Parameters:
    optional: STRING - Output frequency (year, month)
    """
    operator = CdoOperator(command="eca_fd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
