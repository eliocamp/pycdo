
from ..cdo_operator import CdoOperator
inf=float("inf")
def setrtoc2(self, optional):
    r"""
    CDO operator: setrtoc2
Parameters:
    optional: ['FLOAT - Pairs of old and new values', 'FLOAT - Pairs of old and new values', 'FLOAT - Lower bound', 'FLOAT - Upper bound', 'FLOAT - New value - inside range', 'FLOAT - New value - outside range']
    """
    operator = CdoOperator(command="setrtoc2",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
