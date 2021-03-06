# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_containers.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBinary, CPyObject
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class ListOptionalBinaryHelper:
    c_data_set = MultiSet()

    @staticmethod
    def check_c_data_set_empty():
        assert len(ListOptionalBinaryHelper.c_data_set) == 0

    @ffi.callback("struct DjinniBinary *(struct DjinniObjectHandle *, size_t)")
    def __get_elem(cself, index):
        try:
            with CPyBinary.fromPyOpt(CPyObject.toPy(None, cself)[index]) as py_obj:
                return py_obj.release_djinni_binary()
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("size_t(struct DjinniObjectHandle *)")
    def __get_size(cself):
        return len(CPyObject.toPy(None, cself))

    @ffi.callback("struct DjinniObjectHandle *()")
    def __python_create():
        c_ptr = ffi.new_handle(list())
        ListOptionalBinaryHelper.c_data_set.add(c_ptr)
        return ffi.cast("struct DjinniObjectHandle *", c_ptr)

    @ffi.callback("void(struct DjinniObjectHandle *, struct DjinniBinary *)")
    def __python_add(cself, el):
        CPyObject.toPy(None, cself).append(CPyBinary.toPyOpt(el))

    @ffi.callback("void(struct DjinniObjectHandle * )")
    def __delete(c_ptr):
        assert c_ptr in ListOptionalBinaryHelper.c_data_set
        ListOptionalBinaryHelper.c_data_set.remove(c_ptr)

    @staticmethod
    def _add_callbacks():
        lib.list_optional_binary_add_callback__get_elem(ListOptionalBinaryHelper.__get_elem)
        lib.list_optional_binary_add_callback___delete(ListOptionalBinaryHelper.__delete)
        lib.list_optional_binary_add_callback__get_size(ListOptionalBinaryHelper.__get_size)
        lib.list_optional_binary_add_callback__python_create(ListOptionalBinaryHelper.__python_create)
        lib.list_optional_binary_add_callback__python_add(ListOptionalBinaryHelper.__python_add)

ListOptionalBinaryHelper._add_callbacks()

