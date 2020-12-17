from django import template

register = template.Library()

@register.filter
def replace_comma(value, arg):
    new_value = str(value).replace(arg, ".")
    return new_value