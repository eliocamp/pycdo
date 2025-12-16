
from ..cdo_operator import CdoOperator
inf=float("inf")
def strwin(self, optional):
    r"""
    CDO operator: strwin
Parameters:
    optional: FLOAT - Horizontal wind speed threshold (m/s, default v = 10.5 m/s)
    """
    operator = CdoOperator(command="strwin",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
