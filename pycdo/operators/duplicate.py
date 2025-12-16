
from ..cdo_operator import CdoOperator
inf=float("inf")
def duplicate(self, optional):
    r"""
    CDO operator: duplicate
Parameters:
    optional: INTEGER - Number of duplicates, default is 2.
    """
    operator = CdoOperator(command="duplicate",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
