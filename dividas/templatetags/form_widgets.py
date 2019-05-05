from django.template import Library

register = Library()


@register.filter
def add_classes(widget, classes):
    widget.field.widget.attrs['class'] = classes
    return widget


@register.filter
def add_placeholder(widget, placeholder):
    widget.field.widget.attrs['placeholder'] = placeholder
    return widget


@register.filter
def add_key_value_attr(widget, key_value):
    attr, value = key_value.split(',')
    widget.field.widget.attrs[attr] = value
    return widget
