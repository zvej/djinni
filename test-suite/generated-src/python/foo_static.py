# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from foo_static.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyBoxedDate, CPyBoxedI64, CPyDate, CPyPrimitive, CPyString

from abc import ABCMeta, abstractmethod
from future.utils import with_metaclass
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

class FooStatic(with_metaclass(ABCMeta)):
    @staticmethod
    def update_static_messg_to(static_string):
        """ Static method with documentation """
        return FooStaticCppProxy.update_static_messg_to(static_string)
    @staticmethod
    def get_static_messg():
        """
         Static method with long documentation
         (Second line of multi-line documentation.
           Indented third line of multi-line documentation.)
        """
        return FooStaticCppProxy.get_static_messg()
    @staticmethod
    def update_static_counter_by(plus):
        return FooStaticCppProxy.update_static_counter_by(plus)
    @staticmethod
    def update_static_counter_to(init):
        return FooStaticCppProxy.update_static_counter_to(init)
    @staticmethod
    def get_static_counter():
        return FooStaticCppProxy.get_static_counter()
    @staticmethod
    def date_id(d):
        return FooStaticCppProxy.date_id(d)
    @staticmethod
    def opt_date_id(od):
        return FooStaticCppProxy.opt_date_id(od)
    @staticmethod
    def opt_i64_id(od):
        return FooStaticCppProxy.opt_i64_id(od)

class FooStaticCppProxy(FooStatic):
    def __init__(self, proxy):
        self._is_cpp_proxy = True
        self._cpp_impl = proxy
    def __del__(self):
        if not lib:
            return
        lib.foo_static___wrapper_dec_ref(self._cpp_impl)

    @staticmethod
    def update_static_messg_to(static_string):
        with CPyString.fromPy(static_string) as pys_static_string:
            _ret_c = lib.cw__foo_static_update_static_messg_to(pys_static_string.release_djinni_string())
            CPyException.toPyCheckAndRaise(_ret_c)
            _ret = CPyString.toPy(_ret_c)
            assert _ret is not None
            return _ret

    @staticmethod
    def get_static_messg():
        _ret_c = lib.cw__foo_static_get_static_messg()
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyString.toPy(_ret_c)
        assert _ret is not None
        return _ret

    @staticmethod
    def update_static_counter_by(plus):
        _ret_c = lib.cw__foo_static_update_static_counter_by(CPyPrimitive.fromPy(plus))
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    @staticmethod
    def update_static_counter_to(init):
        _ret_c = lib.cw__foo_static_update_static_counter_to(CPyPrimitive.fromPy(init))
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    @staticmethod
    def get_static_counter():
        _ret_c = lib.cw__foo_static_get_static_counter()
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyPrimitive.toPy(_ret_c)
        assert _ret is not None
        return _ret

    @staticmethod
    def date_id(d):
        _ret_c = lib.cw__foo_static_date_id(CPyDate.fromPy(d))
        CPyException.toPyCheckAndRaise(_ret_c)
        _ret = CPyDate.toPy(_ret_c)
        assert _ret is not None
        return _ret

    @staticmethod
    def opt_date_id(od):
        with CPyBoxedDate.fromPyOpt(od) as pyopt_od:
            _ret_c = lib.cw__foo_static_opt_date_id(pyopt_od.release_djinni_boxed())
            CPyException.toPyCheckAndRaise(_ret_c)
            _ret = CPyBoxedDate.toPyOpt(_ret_c)
            return _ret

    @staticmethod
    def opt_i64_id(od):
        with CPyBoxedI64.fromPyOpt(od) as pyopt_od:
            _ret_c = lib.cw__foo_static_opt_i64_id(pyopt_od.release_djinni_boxed())
            CPyException.toPyCheckAndRaise(_ret_c)
            _ret = CPyBoxedI64.toPyOpt(_ret_c)
            return _ret

class FooStaticHelper:
    c_data_set = MultiSet()
    @staticmethod
    def toPy(obj):
        if obj == ffi.NULL:
            return None
        return FooStaticCppProxy(obj)

