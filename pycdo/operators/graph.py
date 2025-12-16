
from ..cdo_operator import CdoOperator
inf=float("inf")
def graph(self, optional):
    r"""
    CDO operator: graph
Parameters:
    optional: STRING - Comma-separated list of plot parameters
    """
    operator = CdoOperator(command="graph",
                           n_input=inf, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
