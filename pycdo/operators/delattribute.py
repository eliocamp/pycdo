
from ..cdo_operator import CdoOperator
inf=float("inf")
def delattribute(self, optional):
    r"""
    CDO operator: delattribute
Parameters:
    optional: STRING - Comma-separated list of attributes.
    """
    operator = CdoOperator(command="delattribute",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
