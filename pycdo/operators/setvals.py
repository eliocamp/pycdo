
from ..cdo_operator import CdoOperator
inf=float("inf")
def setvals(self, optional):
    r"""
    CDO operator: setvals
Parameters:
    optional: ['FLOAT - Pairs of old and new values', 'FLOAT - Pairs of old and new values', 'FLOAT - Lower bound', 'FLOAT - Upper bound', 'FLOAT - New value - inside range', 'FLOAT - New value - outside range']
    """
    operator = CdoOperator(command="setvals",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
