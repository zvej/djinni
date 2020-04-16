// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from foo_containers.djinni

#include <iostream> // for debugging
#include <cassert>
#include "wrapper_marshal.hpp"
#include "foo_containers_record.hpp"

#include "dh__foo_containers_record.hpp"
#include "dh__foo_some_other_record.hpp"
#include "dh__list_binary.hpp"
#include "dh__list_date.hpp"
#include "dh__list_int32_t.hpp"
#include "dh__list_list_string.hpp"
#include "dh__list_optional_binary.hpp"
#include "dh__list_record_foo_some_other_record.hpp"
#include "dh__list_string.hpp"
#include "dh__map_boxed_int32_t_set_string.hpp"
#include "dh__map_int8_t_list_date.hpp"
#include "dh__map_int8_t_set_string.hpp"
#include "dh__map_optional_string_optional_string.hpp"
#include "dh__map_string_int32_t.hpp"
#include "dh__map_string_string.hpp"
#include "dh__set_optional_string.hpp"
#include "dh__set_string.hpp"
#include <chrono>
#include <experimental/optional>
#include <vector>

static void(*s_py_callback_map_string_string___delete)(DjinniObjectHandle *);
void map_string_string_add_callback___delete(void(* ptr)(DjinniObjectHandle *)) {
    s_py_callback_map_string_string___delete = ptr;
}

void map_string_string___delete(DjinniObjectHandle * drh) {
    s_py_callback_map_string_string___delete(drh);
}
void optional_map_string_string___delete(DjinniOptionalObjectHandle *  drh) {
    s_py_callback_map_string_string___delete((DjinniObjectHandle *) drh);
}
static DjinniString * ( * s_py_callback_map_string_string__get_value)(DjinniObjectHandle *, DjinniString *);

void map_string_string_add_callback__get_value(DjinniString *( * ptr)(DjinniObjectHandle *, DjinniString *)) {
    s_py_callback_map_string_string__get_value = ptr;
}

static size_t ( * s_py_callback_map_string_string__get_size)(DjinniObjectHandle *);

void map_string_string_add_callback__get_size(size_t( * ptr)(DjinniObjectHandle *)) {
    s_py_callback_map_string_string__get_size = ptr;
}

static DjinniObjectHandle * ( * s_py_callback_map_string_string__python_create)(void);

void map_string_string_add_callback__python_create(DjinniObjectHandle *( * ptr)(void)) {
    s_py_callback_map_string_string__python_create = ptr;
}

static void ( * s_py_callback_map_string_string__python_add)(DjinniObjectHandle *, DjinniString *, DjinniString *);

void map_string_string_add_callback__python_add(void( * ptr)(DjinniObjectHandle *, DjinniString *, DjinniString *)) {
    s_py_callback_map_string_string__python_add = ptr;
}

static DjinniString * ( * s_py_callback_map_string_string__python_next)(DjinniObjectHandle *);

void map_string_string_add_callback__python_next(DjinniString *( * ptr)(DjinniObjectHandle *)) {
    s_py_callback_map_string_string__python_next = ptr;
}

djinni::Handle<DjinniObjectHandle> DjinniMapStringString::fromCpp(const std::unordered_map<std::string, std::string> & dc) {
    djinni::Handle<DjinniObjectHandle> _handle(s_py_callback_map_string_string__python_create(), & map_string_string___delete);
    for (const auto & it : dc) {
        auto _key = DjinniString::fromCpp(it.first);
        auto _val = DjinniString::fromCpp(it.second);
        s_py_callback_map_string_string__python_add(_handle.get(), _key.release(), _val.release());
    }

    return _handle;
}

std::unordered_map<std::string, std::string> DjinniMapStringString::toCpp(djinni::Handle<DjinniObjectHandle> dh) {
    std::unordered_map<std::string, std::string>_ret;
    size_t size = s_py_callback_map_string_string__get_size(dh.get());

    for (int i = 0; i < size; i++) {
        auto _key_c = std::unique_ptr<DjinniString>(s_py_callback_map_string_string__python_next(dh.get())); // key that would potentially be surrounded by unique pointer
        auto _val = DjinniString::toCpp(std::unique_ptr<DjinniString>(s_py_callback_map_string_string__get_value(dh.get(), _key_c.get())));

        auto _key = DjinniString::toCpp(std::move(_key_c));
        _ret.emplace(std::move(_key), std::move(_val));
    }

    return _ret;
}

djinni::Handle<DjinniOptionalObjectHandle> DjinniMapStringString::fromCpp(std::experimental::optional<std::unordered_map<std::string, std::string>> dc) {
    if (dc == std::experimental::nullopt) {
        return nullptr;
    }
    return djinni::optionals::toOptionalHandle(DjinniMapStringString::fromCpp(std::move(* dc)), optional_map_string_string___delete);
}

std::experimental::optional<std::unordered_map<std::string, std::string>>DjinniMapStringString::toCpp(djinni::Handle<DjinniOptionalObjectHandle> dh) {
     if (dh) {
        return std::experimental::optional<std::unordered_map<std::string, std::string>>(DjinniMapStringString::toCpp(djinni::optionals::fromOptionalHandle(std::move(dh), map_string_string___delete)));
    }
    return std::experimental::nullopt;
}

