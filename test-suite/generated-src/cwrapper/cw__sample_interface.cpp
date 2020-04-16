// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from test.djinni

#include <iostream> // for debugging
#include <cassert>
#include "wrapper_marshal.hpp"
#include "sample_interface.hpp"

#include "cw__sample_interface.hpp"

std::shared_ptr<::testsuite::SampleInterface> DjinniWrapperSampleInterface::get(djinni::WrapperRef<DjinniWrapperSampleInterface> dw) {
    if (dw) {
        return dw->wrapped_obj;
    }
    return nullptr;
}

void sample_interface___wrapper_add_ref(DjinniWrapperSampleInterface * dh) {
    dh->ref_count.fetch_add(1);
}
void sample_interface___wrapper_dec_ref(DjinniWrapperSampleInterface * dh) {
    const size_t ref = dh->ref_count.fetch_sub(1);
    if (ref == 1) {// value before sub is returned
        delete dh;
    }
}
djinni::Handle<DjinniWrapperSampleInterface> DjinniWrapperSampleInterface::wrap(std::shared_ptr<::testsuite::SampleInterface> obj) {
    if (obj)
        return djinni::Handle<DjinniWrapperSampleInterface>(new DjinniWrapperSampleInterface{ std::move(obj) }, sample_interface___wrapper_dec_ref);
    return nullptr;
}

