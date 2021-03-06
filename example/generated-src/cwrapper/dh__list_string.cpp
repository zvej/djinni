// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#include <iostream> // for debugging
#include <cassert>
#include "wrapper_marshal.hpp"
#include "item_list.hpp"

#include "dh__item_list.hpp"
#include "dh__list_string.hpp"

static void(*s_py_callback_list_string___delete)(DjinniObjectHandle *);
void list_string_add_callback___delete(void(* ptr)(DjinniObjectHandle *)) {
    s_py_callback_list_string___delete = ptr;
}

void list_string___delete(DjinniObjectHandle * drh) {
    s_py_callback_list_string___delete(drh);
}
void optional_list_string___delete(DjinniOptionalObjectHandle *  drh) {
    s_py_callback_list_string___delete((DjinniObjectHandle *) drh);
}
static DjinniString * ( * s_py_callback_list_string__get_elem)(DjinniObjectHandle *, size_t);

void list_string_add_callback__get_elem(DjinniString *( * ptr)(DjinniObjectHandle *, size_t)) {
    s_py_callback_list_string__get_elem = ptr;
}

static size_t ( * s_py_callback_list_string__get_size)(DjinniObjectHandle *);

void list_string_add_callback__get_size(size_t( * ptr)(DjinniObjectHandle *)) {
    s_py_callback_list_string__get_size = ptr;
}

static DjinniObjectHandle * ( * s_py_callback_list_string__python_create)(void);

void list_string_add_callback__python_create(DjinniObjectHandle *( * ptr)(void)) {
    s_py_callback_list_string__python_create = ptr;
}

static void ( * s_py_callback_list_string__python_add)(DjinniObjectHandle *, DjinniString *);

void list_string_add_callback__python_add(void( * ptr)(DjinniObjectHandle *, DjinniString *)) {
    s_py_callback_list_string__python_add = ptr;
}

djinni::Handle<DjinniObjectHandle> DjinniListString::fromCpp(const std::vector<std::string> & dc) {
    djinni::Handle<DjinniObjectHandle> _handle(s_py_callback_list_string__python_create(), & list_string___delete);
    size_t size = dc.size();
    for (int i = 0; i < size; i++) {
        auto _el = DjinniString::fromCpp(dc[i]);
        s_py_callback_list_string__python_add(_handle.get(), _el.release());
    }

    return _handle;
}

std::vector<std::string> DjinniListString::toCpp(djinni::Handle<DjinniObjectHandle> dh) {
    std::vector<std::string>_ret;
    size_t size = s_py_callback_list_string__get_size(dh.get());
    _ret.reserve(size);

    for (int i = 0; i < size; i++) {
        _ret.push_back(DjinniString::toCpp(std::unique_ptr<DjinniString>(s_py_callback_list_string__get_elem(dh.get(), i))));
    }

    return _ret;
}

djinni::Handle<DjinniOptionalObjectHandle> DjinniListString::fromCpp(std::experimental::optional<std::vector<std::string>> dc) {
    if (dc == std::experimental::nullopt) {
        return nullptr;
    }
    return djinni::optionals::toOptionalHandle(DjinniListString::fromCpp(std::move(* dc)), optional_list_string___delete);
}

std::experimental::optional<std::vector<std::string>>DjinniListString::toCpp(djinni::Handle<DjinniOptionalObjectHandle> dh) {
     if (dh) {
        return std::experimental::optional<std::vector<std::string>>(DjinniListString::toCpp(djinni::optionals::fromOptionalHandle(std::move(dh), list_string___delete)));
    }
    return std::experimental::nullopt;
}

