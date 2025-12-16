
from ..cdo_operator import CdoOperator
inf=float("inf")
def vertfillmiss(self, optional):
    r"""
    CDO operator: vertfillmiss
Parameters:
    optional: ['STRING - Fill method \\[nearest|linear|forward|backward\\] (default: nearest)', 'INTEGER - The maximum number of consecutive missing values to fill (default: all)', 'INTEGER - The maximum number of gaps to fill (default: all)']
    """
    operator = CdoOperator(command="vertfillmiss",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
