
from ..cdo_operator import CdoOperator
inf=float("inf")
def splitname(self, optional):
    r"""
    CDO operator: splitname
Parameters:
    optional: ['STRING - Swap the position of obase and xxx in the output filename', 'STRING - Add a UUID as global attribute <attname> to each output file']
    """
    operator = CdoOperator(command="splitname",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
