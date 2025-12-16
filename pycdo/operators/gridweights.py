
from ..cdo_operator import CdoOperator
inf=float("inf")
def gridweights(self, optional):
    r"""
    CDO operator: gridweights
Parameters:
    optional: FLOAT - Planet radius in meter
    """
    operator = CdoOperator(command="gridweights",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
