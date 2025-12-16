
from ..cdo_operator import CdoOperator
inf=float("inf")
def setfilter(self, optional):
    r"""
    CDO operator: setfilter
Parameters:
    optional: STRING - Read filter specification per variable from file \[format: varname=\"<filterspec>\"\]
    """
    operator = CdoOperator(command="setfilter",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
