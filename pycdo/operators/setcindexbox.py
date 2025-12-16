
from ..cdo_operator import CdoOperator
inf=float("inf")
def setcindexbox(self, optional):
    r"""
    CDO operator: setcindexbox
Parameters:
    optional: ['FLOAT - Constant', 'FLOAT - Western longitude', 'FLOAT - Eastern longitude', 'FLOAT - Southern or northern latitude', 'FLOAT - Northern or southern latitude', 'INTEGER - Index of first longitude', 'INTEGER - Index of last longitude', 'INTEGER - Index of first latitude', 'INTEGER - Index of last latitude']
    """
    operator = CdoOperator(command="setcindexbox",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
