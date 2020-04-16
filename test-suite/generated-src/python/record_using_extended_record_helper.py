# AUTOGENERATED FILE - DO NOT MODIFY!
# This file generated by Djinni from extended_record.djinni

from djinni.support import MultiSet # default imported in all files
from djinni.exception import CPyException # default imported in all files
from djinni.pycffi_marshal import CPyRecord

from extended_record import ExtendedRecord
from extended_record_helper import ExtendedRecordHelper
from PyCFFIlib_cffi import ffi, lib

from djinni import exception # this forces run of __init__.py which gives cpp option to call back into py to create exception

from record_using_extended_record import RecordUsingExtendedRecord

class RecordUsingExtendedRecordHelper:
    @staticmethod
    def release(c_ptr):
        assert c_ptr in c_data_set
        c_data_set.remove(ffi.cast("void*", c_ptr))

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniRecordHandle *)")
    def get_record_using_extended_record_f1(cself):
        try:
            _ret = CPyRecord.fromPy(ExtendedRecord.c_data_set, CPyRecord.toPy(None, cself).er)
            assert _ret != ffi.NULL
            return _ret
        except Exception as _djinni_py_e:
            CPyException.setExceptionFromPy(_djinni_py_e)
            return ffi.NULL

    @ffi.callback("struct DjinniRecordHandle *(struct DjinniRecordHandle *)")
    def python_create_record_using_extended_record(er):
        py_rec = RecordUsingExtendedRecord(
            CPyRecord.toPy(ExtendedRecord.c_data_set, er))
        return CPyRecord.fromPy(RecordUsingExtendedRecord.c_data_set, py_rec) #to do: can be optional?

    @ffi.callback("void (struct DjinniRecordHandle *)")
    def __delete(dh):
        assert dh in RecordUsingExtendedRecord.c_data_set
        RecordUsingExtendedRecord.c_data_set.remove(dh)

    @staticmethod
    def _add_callbacks():
        lib.record_using_extended_record_add_callback_get_record_using_extended_record_f1(RecordUsingExtendedRecordHelper.get_record_using_extended_record_f1)
        lib.record_using_extended_record_add_callback___delete(RecordUsingExtendedRecordHelper.__delete)
        lib.record_using_extended_record_add_callback_python_create_record_using_extended_record(RecordUsingExtendedRecordHelper.python_create_record_using_extended_record)

RecordUsingExtendedRecord.CR = RecordUsingExtendedRecord(
    RecordUsingExtendedRecord.CR = ExtendedRecord(
        False)
)


RecordUsingExtendedRecordHelper._add_callbacks()

