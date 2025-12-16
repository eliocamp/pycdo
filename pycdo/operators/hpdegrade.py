
from ..cdo_operator import CdoOperator
inf=float("inf")
def hpdegrade(self, optional):
    r"""
    CDO operator: hpdegrade
Parameters:
    optional: ['INTEGER - The nside of the target healpix, must be a power of two \\[default: same as input\\].', "STRING - Pixel ordering of the target healpix ('nested' or 'ring').", 'FLOAT - If non-zero, divide the result by (nside\\[in\\]/nside\\[out\\])**power. power=-2 keeps the sum of the map invariant.']
    """
    operator = CdoOperator(command="hpdegrade",
                           n_input=1, 
                           n_output=1, 
                           params=['optional'])
    return self._new_op(operator, [], {"optional": optional})
