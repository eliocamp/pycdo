
from ..cdo_operator import CdoOperator
inf=float("inf")
def showattribute(self, optional):
    r"""
    CDO operator: showattribute
Parameters:
    optional: STRING - Comma-separated list of attributes.
    """
    operator = CdoOperator(command="showattribute",
                           n_input=1, 
                           n_output=0, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
