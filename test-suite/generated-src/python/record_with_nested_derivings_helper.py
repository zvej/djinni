# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from derivings.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyPrimitive, CPyRecord

from record_with_derivings import RecordWithDerivings
from record_with_derivings_helper import RecordWithDerivingsHelper
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from record_with_nested_derivings import RecordWithNestedDerivings

class RecordWithNestedDerivingsHelper:
    @staticmethod
    def release(c_ptr):
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("int32_t(struct DjinniRecordHandle *)")
    def get_record_with_nested_derivings_f1(cself):
        try:
            _ret = CPyPrimitive.fromPy(CPyRecord.toPy(None, cself).key)
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniRecordHandle *)")
    def get_record_with_nested_derivings_f2(cself):
        try:
            _ret = CPyRecord.fromPy(RecordWithDerivings.c_data_set, CPyRecord.toPy(None, cself).rec)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(int32_t,struct DjinniRecordHandle *)")
    def python_create_record_with_nested_derivings(key,rec):
        py_rec = RecordWithNestedDerivings(
            CPyPrimitive.toPy(key),
            CPyRecord.toPy(RecordWithDerivings.c_data_set, rec))
        return CPyRecord.fromPy(RecordWithNestedDerivings.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in RecordWithNestedDerivings.c_data_set
        RecordWithNestedDerivings.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.record_with_nested_derivings_add_callback_get_record_with_nested_derivings_f2(RecordWithNestedDerivingsHelper.get_record_with_nested_derivings_f2)
        lib.record_with_nested_derivings_add_callback___delete(RecordWithNestedDerivingsHelper.__delete)
        lib.record_with_nested_derivings_add_callback_python_create_record_with_nested_derivings(RecordWithNestedDerivingsHelper.python_create_record_with_nested_derivings)
        lib.record_with_nested_derivings_add_callback_get_record_with_nested_derivings_f1(RecordWithNestedDerivingsHelper.get_record_with_nested_derivings_f1)

RecordWithNestedDerivingsHelper._add_callbacks()

