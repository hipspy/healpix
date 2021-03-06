# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
BSD-licensed HEALPix for Astropy.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
from ._astropy_init import *  # noqa

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:  # noqa
    from .high_level import *  # noqa
    from .core import *  # noqa
