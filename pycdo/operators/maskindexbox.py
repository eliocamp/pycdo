
from ..cdo_operator import CdoOperator
inf=float("inf")
def maskindexbox(self, optional):
    r"""
    CDO operator: maskindexbox
Parameters:
    optional: ['FLOAT - Western longitude', 'FLOAT - Eastern longitude', 'FLOAT - Southern or northern latitude', 'FLOAT - Northern or southern latitude', 'INTEGER - Index of first longitude', 'INTEGER - Index of last longitude', 'INTEGER - Index of first latitude', 'INTEGER - Index of last latitude']
    """
    operator = CdoOperator(command="maskindexbox",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
