"""
This module contains utilities for Monte Carlo simulation.
"""

import numpy as np


def antithetic_normal(rng, n, scale, out):
    """Generate antithetic normal random numbers.

    Args:
        rng: The random number generator.
        n: The number of random numbers to generate.
        scale: scaling factor to apply.
        out: The destination array of size 2n.

    """
    rng.standard_normal(n, out=out[0:n])
    np.multiply(scale, out[0:n], out=out[0:n])
    np.negative(out[0:n], out=out[n:])
