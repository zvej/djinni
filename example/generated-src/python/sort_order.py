# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from example.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from enum import IntEnum, unique

@unique
class SortOrder(IntEnum):
    Ascending = 0
    Descending = 1
    Random = 2
