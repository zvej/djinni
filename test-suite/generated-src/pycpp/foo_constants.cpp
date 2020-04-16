// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_constants.djinni

#include "foo_constants.hpp"  // my header

namespace testsuite {

bool constexpr FooConstants::BOOL_CONSTANT;

int8_t constexpr FooConstants::I8_CONSTANT;

int16_t constexpr FooConstants::I16_CONSTANT;

int32_t constexpr FooConstants::I32_CONSTANT;

int64_t constexpr FooConstants::I64_CONSTANT;

float constexpr FooConstants::F32_CONSTANT;

double constexpr FooConstants::F64_CONSTANT;

std::string const FooConstants::STRING_CONSTANT = {"string-constant"};

std::experimental::optional<int32_t> const FooConstants::OPTIONAL_INTEGER_CONSTANT = 1;

FooConstants const FooConstants::OBJECT_CONSTANT = FooConstants(
    FooConstants::I32_CONSTANT /* some_integer */ ,
    FooConstants::STRING_CONSTANT /* some_string */ );

SomeConstRecord const FooConstants::SOME_RECORD = SomeConstRecord(
    28 /* number1 */ ,
    FooConstants::I16_CONSTANT /* number2 */ );

}  // namespace testsuite
