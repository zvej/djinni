// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_primitives.djinni

#pragma once

#include <atomic>
#include <experimental/optional>
#include "foo_primitives.hpp"
#ifdef __cplusplus
extern "C" {
#endif

#include "cw__foo_primitives.h"

#ifdef __cplusplus
}
#endif
struct DjinniWrapperFooPrimitives final {
    DjinniWrapperFooPrimitives(std::shared_ptr<::testsuite::FooPrimitives>wo): wrapped_obj(wo) {};

    static std::shared_ptr<::testsuite::FooPrimitives> get(djinni::Handle<DjinniWrapperFooPrimitives> dw);
    static djinni::Handle<DjinniWrapperFooPrimitives> wrap(std::shared_ptr<::testsuite::FooPrimitives> obj);

    const std::shared_ptr<::testsuite::FooPrimitives> wrapped_obj;
    std::atomic<size_t> ref_count {1};
};
