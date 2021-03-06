// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_containers.djinni

#pragma once

#include <atomic>
#include <experimental/optional>
#include "foo_containers_record.hpp"
#ifdef __cplusplus
extern "C" {
#endif

#include "dh__list_date.h"

#ifdef __cplusplus
}
#endif
struct DjinniListDate {
    static djinni::Handle<DjinniObjectHandle> fromCpp(const std::vector<std::chrono::system_clock::time_point> & dc);
    static std::vector<std::chrono::system_clock::time_point> toCpp(djinni::Handle<DjinniObjectHandle> dh);
    static djinni::Handle<DjinniOptionalObjectHandle>fromCpp(std::experimental::optional<std::vector<std::chrono::system_clock::time_point>> dc);
    static std::experimental::optional<std::vector<std::chrono::system_clock::time_point>> toCpp(djinni::Handle<DjinniOptionalObjectHandle> dh);
};
