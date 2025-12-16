
from ..cdo_operator import CdoOperator
inf=float("inf")
def bitrounding(self, optional):
    r"""
    CDO operator: bitrounding
Parameters:
    optional: ['FLOAT - Information level (0 - 1) \\[default: 0.9999\\]', 'INTEGER - Add bits to the number of significant bits \\[default: 0\\]', 'INTEGER - Minimum value of the number of bits \\[default: 1\\]', 'INTEGER - Maximum value of the number of bits \\[default: 23\\]', 'INTEGER - Set to 1 to run the calculation only in the first time step', 'INTEGER - Set number of significant bits', 'BOOL - Print max. numbits per variable of 1st timestep to stdout \\[format: name=numbits\\]', 'STRING - Read number of significant bits per variable from file \\[format: name=numbits\\]']
    """
    operator = CdoOperator(command="bitrounding",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
