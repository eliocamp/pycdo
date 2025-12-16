
from ..cdo_operator import CdoOperator
inf=float("inf")
def sethalo(self, optional):
    r"""
    CDO operator: sethalo
Parameters:
    optional: ['INTEGER - East halo', 'INTEGER - West halo', 'INTEGER - South halo', 'INTEGER - North halo', 'FLOAT - Fill value (default is the missing value)']
    """
    operator = CdoOperator(command="sethalo",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
