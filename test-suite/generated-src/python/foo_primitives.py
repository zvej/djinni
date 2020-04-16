# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_primitives.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBinary, CPyDate, CPyPrimitive, CPyString

from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class FooPrimitives(with_metaclass(ABCMeta)):
    @abstractmethod
    def set_int8(self, private_int):
        raise NotImplementedError

    @abstractmethod
    def get_int8(self):
        raise NotImplementedError

    @abstractmethod
    def set_int16(self, private_int):
        raise NotImplementedError

    @abstractmethod
    def get_int16(self):
        raise NotImplementedError

    @abstractmethod
    def set_int32(self, private_int):
        raise NotImplementedError

    @abstractmethod
    def get_int32(self):
        raise NotImplementedError

    @abstractmethod
    def set_int64(self, private_int):
        raise NotImplementedError

    @abstractmethod
    def get_int64(self):
        raise NotImplementedError

    @abstractmethod
    def set_float(self, private_float):
        raise NotImplementedError

    @abstractmethod
    def get_float(self):
        raise NotImplementedError

    @abstractmethod
    def set_double(self, private_double):
        raise NotImplementedError

    @abstractmethod
    def get_double(self):
        raise NotImplementedError

    @abstractmethod
    def set_bool(self, private_bool):
        raise NotImplementedError

    @abstractmethod
    def get_bool(self):
        raise NotImplementedError

    @abstractmethod
    def set_binary(self, private_binary):
        raise NotImplementedError

    @abstractmethod
    def get_binary(self):
        raise NotImplementedError

    @abstractmethod
    def set_string(self, private_string):
        raise NotImplementedError

    @abstractmethod
    def get_string(self):
        raise NotImplementedError

    @abstractmethod
    def set_date(self, private_date):
        raise NotImplementedError

    @abstractmethod
    def get_date(self):
        raise NotImplementedError

    @staticmethod
    def create():
        return FooPrimitivesCppProxy.create()

class FooPrimitivesCppProxy(FooPrimitives):
    def __init__(self, proxy):
        self._is_cpp_proxy = True
        self._cpp_impl = proxy
    def __del__(self):
        if not lib:
            return
        lib.foo_primitives___wrapper_dec_ref(self._cpp_impl)

    def set_int8(self, private_int):
        lib.cw__foo_primitives_set_int8(self._cpp_impl, CPyPrimitive.fromPy(private_int))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_int8(self):
        _ret_c = lib.cw__foo_primitives_get_int8(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_int16(self, private_int):
        lib.cw__foo_primitives_set_int16(self._cpp_impl, CPyPrimitive.fromPy(private_int))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_int16(self):
        _ret_c = lib.cw__foo_primitives_get_int16(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_int32(self, private_int):
        lib.cw__foo_primitives_set_int32(self._cpp_impl, CPyPrimitive.fromPy(private_int))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_int32(self):
        _ret_c = lib.cw__foo_primitives_get_int32(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_int64(self, private_int):
        lib.cw__foo_primitives_set_int64(self._cpp_impl, CPyPrimitive.fromPy(private_int))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_int64(self):
        _ret_c = lib.cw__foo_primitives_get_int64(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_float(self, private_float):
        lib.cw__foo_primitives_set_float(self._cpp_impl, CPyPrimitive.fromPy(private_float))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_float(self):
        _ret_c = lib.cw__foo_primitives_get_float(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_double(self, private_double):
        lib.cw__foo_primitives_set_double(self._cpp_impl, CPyPrimitive.fromPy(private_double))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_double(self):
        _ret_c = lib.cw__foo_primitives_get_double(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_bool(self, private_bool):
        lib.cw__foo_primitives_set_bool(self._cpp_impl, CPyPrimitive.fromPy(private_bool))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_bool(self):
        _ret_c = lib.cw__foo_primitives_get_bool(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_binary(self, private_binary):
        with CPyBinary.fromPy(private_binary) as pybin_private_binary:
            lib.cw__foo_primitives_set_binary(self._cpp_impl, pybin_private_binary.release_djinni_binary())
            CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_binary(self):
        _ret_c = lib.cw__foo_primitives_get_binary(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyBinary.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_string(self, private_string):
        with CPyString.fromPy(private_string) as pys_private_string:
            lib.cw__foo_primitives_set_string(self._cpp_impl, pys_private_string.release_djinni_string())
            CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_string(self):
        _ret_c = lib.cw__foo_primitives_get_string(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyString.toPy(_ret_c)
        assert _ret is not None
        return _ret

    def set_date(self, private_date):
        lib.cw__foo_primitives_set_date(self._cpp_impl, CPyDate.fromPy(private_date))
        CPyException.toPyCheckAndRaise(ffi.NULL)

    def get_date(self):
        _ret_c = lib.cw__foo_primitives_get_date(self._cpp_impl)
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyDate.toPy(_ret_c)
        assert _ret is not None
        return _ret

    @staticmethod
    def create():
        _ret_c = lib.cw__foo_primitives_create()
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = FooPrimitivesHelper.toPy(_ret_c)
        assert _ret is not None
        return _ret

class FooPrimitivesHelper:
    c_data_set = MultiSet()
    @staticmethod
    def toPy(obj):
        if obj == ffi.NULL:
            return None
        return FooPrimitivesCppProxy(obj)

