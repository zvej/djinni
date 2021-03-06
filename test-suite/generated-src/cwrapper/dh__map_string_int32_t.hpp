// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_containers.djinni

#pragma once

#include <atomic>
#include <experimental/optional>
#include "foo_containers_record.hpp"
#ifdef __cplusplus
extern "C" {
#endif

#include "dh__map_string_int32_t.h"

#ifdef __cplusplus
}
#endif
struct DjinniMapStringInt32T {
    static djinni::Handle<DjinniObjectHandle> fromCpp(const std::unordered_map<std::string, int32_t> & dc);
    static std::unordered_map<std::string, int32_t> toCpp(djinni::Handle<DjinniObjectHandle> dh);
    static djinni::Handle<DjinniOptionalObjectHandle>fromCpp(std::experimental::optional<std::unordered_map<std::string, int32_t>> dc);
    static std::experimental::optional<std::unordered_map<std::string, int32_t>> toCpp(djinni::Handle<DjinniOptionalObjectHandle> dh);
};
