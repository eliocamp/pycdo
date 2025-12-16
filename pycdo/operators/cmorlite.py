
from ..cdo_operator import CdoOperator
inf=float("inf")
def cmorlite(self, optional):
    r"""
    CDO operator: cmorlite
Parameters:
    optional: ['STRING - Name of the CMOR table as specified from PCMDI', 'STRING - Converts the units if necessary']
    """
    operator = CdoOperator(command="cmorlite",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
