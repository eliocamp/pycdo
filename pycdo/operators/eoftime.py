
from ..cdo_operator import CdoOperator
inf=float("inf")
def eoftime(self, optional):
    r"""
    CDO operator: eoftime
Parameters:
    optional: INTEGER - Number of eigen functions
    """
    operator = CdoOperator(command="eoftime",
                           n_input=1, 
                           n_output=2, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
