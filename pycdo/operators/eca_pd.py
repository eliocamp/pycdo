
from ..cdo_operator import CdoOperator
inf=float("inf")
def eca_pd(self, optional):
    r"""
    CDO operator: eca_pd
Parameters:
    optional: ['FLOAT - Daily precipitation amount threshold in \\[mm\\]', 'STRING - Output frequency (year, month)']
    """
    operator = CdoOperator(command="eca_pd",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
