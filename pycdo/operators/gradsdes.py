
from ..cdo_operator import CdoOperator
inf=float("inf")
def gradsdes(self, optional):
    r"""
    CDO operator: gradsdes
Parameters:
    optional: INTEGER - Format version of the GrADS map file for GRIB1 datasets. Use 1 for a machinespecific version 1 GrADS map file, 2 for a machine independent version 2 GrADS map fileand 4 to support GRIB files >2GB.A version 2 map file can be used only with GrADS version 1.8 or newer.A version 4 map file can be used only with GrADS version 2.0 or newer.The default is 4 for files >2GB, otherwise 2.
    """
    operator = CdoOperator(command="gradsdes",
                           n_input=1, 
                           n_output=0, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
