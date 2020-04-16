# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from enum.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from enum import IntEnum, unique

@unique
class Color(IntEnum):
    Red = 0
    Orange = 1
    Yellow = 2
    Green = 3
    Blue = 4
    """
     "It is customary to list indigo as a color lying between blue and violet, but it has
     never seemed to me that indigo is worth the dignity of being considered a separate
     color. To my eyes it seems merely deep blue." --Isaac Asimov
    """
    Indigo = 5
    Violet = 6
