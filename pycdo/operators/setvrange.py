
from ..cdo_operator import CdoOperator
inf=float("inf")
def setvrange(self, optional):
    r"""
    CDO operator: setvrange
Parameters:
    optional: ['INTEGER - Number of nearest neighbors', 'FLOAT - New missing value', 'FLOAT - Constant', 'FLOAT - Lower bound', 'FLOAT - Upper bound']
    """
    operator = CdoOperator(command="setvrange",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
