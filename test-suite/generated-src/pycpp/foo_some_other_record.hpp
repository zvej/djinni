// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_client_interface.djinni

#pragma once

#include <cstdint>
#include <utility>

namespace testsuite {

struct FooSomeOtherRecord final {
    int64_t number1;
    int32_t number2;

    friend bool operator==(const FooSomeOtherRecord& lhs, const FooSomeOtherRecord& rhs);
    friend bool operator!=(const FooSomeOtherRecord& lhs, const FooSomeOtherRecord& rhs);

    friend bool operator<(const FooSomeOtherRecord& lhs, const FooSomeOtherRecord& rhs);
    friend bool operator>(const FooSomeOtherRecord& lhs, const FooSomeOtherRecord& rhs);

    friend bool operator<=(const FooSomeOtherRecord& lhs, const FooSomeOtherRecord& rhs);
    friend bool operator>=(const FooSomeOtherRecord& lhs, const FooSomeOtherRecord& rhs);

    FooSomeOtherRecord(int64_t number1_,
                       int32_t number2_)
    : number1(std::move(number1_))
    , number2(std::move(number2_))
    {}
};

}  // namespace testsuite
