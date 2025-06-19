
from ..cdo_operator import CdoOperator
inf=float("inf")
def sellonlatbox(self, lon1, lon2, lat1, lat2):
    """
    CDO operator: sellonlatbox
Parameters:
    lon1: left longitude
    lon2: right longitude
    lat1: lower latitude
    lat2: upper latitude
    """
    operator = CdoOperator(name="sellonlatbox",
                           num_inputs=1, 
                           num_outputs=1, 
                           parameters=[lon1, lon2, lat1, lat2])
    return self._new_op(operator, [], {"lon1": lon1, "lon2": lon2, "lat1": lat1, "lat2": lat2})
