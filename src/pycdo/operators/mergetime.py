
from cdo_operator import CdoOperator
inf=float("inf")
def mergetime(self, ):
    """
     
    """
    operator = CdoOperator(name="mergetime",
                           num_inputs=inf, 
                           num_outputs=1, 
                           parameters=[])
    return self._new_op(operator, [], {})
