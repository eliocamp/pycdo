
from ..cdo_operator import CdoOperator
inf=float("inf")
def splitcode(self, optional):
    r"""
    CDO operator: splitcode
Parameters:
    optional: ['STRING - Swap the position of obase and xxx in the output filename', 'STRING - Add a UUID as global attribute <attname> to each output file']
    """
    operator = CdoOperator(command="splitcode",
                           n_input=1, 
                           n_output=inf, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
