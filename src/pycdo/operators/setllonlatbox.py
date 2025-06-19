
from cdo_operator import CdoOperator
inf=float("inf")
def setllonlatbox(self, lon1, lon2, lat1, lat2):
    """
     
    """
    operator = CdoOperator(name="setllonlatbox",
                           num_inputs=1, 
                           num_outputs=1, 
                           parameters=[lon1, lon2, lat1, lat2])
    return self._new_op(operator, [], {"lon1": lon1, "lon2": lon2, "lat1": lat1, "lat2": lat2})
