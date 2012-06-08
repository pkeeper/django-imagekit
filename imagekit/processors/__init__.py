"""
Imagekit image processors.

A processor accepts an image, does some stuff, and returns the result.
Processors can do anything with the image you want, but their responsibilities
should be limited to image manipulations--they should be completely decoupled
from both the filesystem and the ORM.

"""

from imagekit.processors.base import *
from imagekit.processors.crop import *
from imagekit.processors.resize import *
