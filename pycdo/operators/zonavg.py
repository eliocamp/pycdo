
from ..cdo_operator import CdoOperator
inf=float("inf")
def zonavg(self, optional):
    r"""
    CDO operator: zonavg
Parameters:
    optional: ['FLOAT - Percentile number in \\{0, ..., 100\\}', 'STRING - Description of the zonal latitude bins needed for data on an unstructured grid. A predefined zonal description is zonal_<DY>. DY is the increment of the latitudes in degrees.']
    """
    operator = CdoOperator(command="zonavg",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
