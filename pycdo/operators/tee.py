
from ..cdo_operator import CdoOperator
inf=float("inf")
def tee(self, optional):
    r"""
    CDO operator: tee
Parameters:
    optional: STRING - Destination filename for the copy of the input file
    """
    operator = CdoOperator(command="tee",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
