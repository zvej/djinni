// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from example.djinni

#pragma once // python_cdef_ignore
#include <stdbool.h>  // python_cdef_ignore

struct DjinniWrapperTextboxListener;
void textbox_listener___delete(struct DjinniObjectHandle * djinni_this);
void textbox_listener___wrapper_dec_ref(struct DjinniWrapperTextboxListener * dh);
void textbox_listener___wrapper_add_ref(struct DjinniWrapperTextboxListener * dh);

struct DjinniWrapperTextboxListener *  make_proxy_object_from_handle_cw__textbox_listener(struct DjinniObjectHandle * c_ptr);
struct DjinniObjectHandle * get_handle_from_proxy_object_cw__textbox_listener(struct DjinniWrapperTextboxListener * dw);
bool equal_handles_cw__textbox_listener(struct DjinniWrapperTextboxListener * dw1, struct DjinniWrapperTextboxListener * dw2);

void textbox_listener_add_callback_update(void(* ptr)(struct DjinniObjectHandle * , struct DjinniRecordHandle *));

void textbox_listener_add_callback___delete(void(* ptr)(struct DjinniObjectHandle * ));