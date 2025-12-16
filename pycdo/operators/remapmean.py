
from ..cdo_operator import CdoOperator
inf=float("inf")
def remapmean(self, optional):
    r"""
    CDO operator: remapmean
Parameters:
    optional: STRING - Target grid description file or name
    """
    operator = CdoOperator(command="remapmean",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
