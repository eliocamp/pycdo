
from ..cdo_operator import CdoOperator
inf=float("inf")
def zonmin(self, optional):
    r"""
    CDO operator: zonmin
Parameters:
    optional: ['FLOAT - Percentile number in \\{0, ..., 100\\}', 'STRING - Description of the zonal latitude bins needed for data on an unstructured grid. A predefined zonal description is zonal_<DY>. DY is the increment of the latitudes in degrees.']
    """
    operator = CdoOperator(command="zonmin",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
