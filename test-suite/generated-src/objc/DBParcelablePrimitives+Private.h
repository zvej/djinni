// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from parcelable.djinni

#import "DBParcelablePrimitives.h"
#include "parcelable_primitives.hpp"

static_assert(__has_feature(objc_arc), "Djinni requires ARC to be enabled for this file");

@class DBParcelablePrimitives;

namespace djinni_generated {

struct ParcelablePrimitives
{
    using CppType = ::testsuite::ParcelablePrimitives;
    using ObjcType = DBParcelablePrimitives*;

    using Boxed = ParcelablePrimitives;

    static CppType toCpp(ObjcType objc);
    static ObjcType fromCpp(const CppType& cpp);
};

}  // namespace djinni_generated
