
from ..cdo_operator import CdoOperator
inf=float("inf")
def outputtab(self, optional):
    r"""
    CDO operator: outputtab
Parameters:
    optional: STRING - Comma-separated list of keynames, one for each column of the table
    """
    operator = CdoOperator(command="outputtab",
                           n_input=inf, 
                           n_output=0, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
