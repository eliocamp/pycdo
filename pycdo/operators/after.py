
from ..cdo_operator import CdoOperator
inf=float("inf")
def after(self, optional):
    r"""
    CDO operator: after
Parameters:
    optional: STRING - File with VCT in ASCII format
    """
    operator = CdoOperator(command="after",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
