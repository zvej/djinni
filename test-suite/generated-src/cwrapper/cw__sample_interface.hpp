// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from test.djinni

#pragma once

#include <atomic>
#include <experimental/optional>
#include "sample_interface.hpp"
#ifdef __cplusplus
extern "C" {
#endif

#include "cw__sample_interface.h"

#ifdef __cplusplus
}
#endif
struct DjinniWrapperSampleInterface final {
    DjinniWrapperSampleInterface(std::shared_ptr<::testsuite::SampleInterface>wo): wrapped_obj(wo) {};

    static std::shared_ptr<::testsuite::SampleInterface> get(djinni::Handle<DjinniWrapperSampleInterface> dw);
    static djinni::Handle<DjinniWrapperSampleInterface> wrap(std::shared_ptr<::testsuite::SampleInterface> obj);

    const std::shared_ptr<::testsuite::SampleInterface> wrapped_obj;
    std::atomic<size_t> ref_count {1};
};
