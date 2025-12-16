
from ..cdo_operator import CdoOperator
inf=float("inf")
def pack(self, optional):
    r"""
    CDO operator: pack
Parameters:
    optional: ['BOOL - Print pack parameters to stdout for each variable', 'STRING - Read pack parameters from file for each variable\\[format: name=<> add_offset=<> scale_factor=<>\\]']
    """
    operator = CdoOperator(command="pack",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
