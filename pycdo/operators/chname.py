
from ..cdo_operator import CdoOperator
inf=float("inf")
def chname(self, optional):
    r"""
    CDO operator: chname
Parameters:
    optional: ['INTEGER - Code number', 'INTEGER - Pairs of old and new code numbers', 'INTEGER - Pairs of old and new code numbers', 'STRING - Pairs of old and new parameter identifiers', 'STRING - Pairs of old and new parameter identifiers', 'STRING - Variable name', 'STRING - Pairs of old and new variable names', 'STRING - Pairs of old and new variable names', 'FLOAT - Old level', 'FLOAT - New level']
    """
    operator = CdoOperator(command="chname",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
