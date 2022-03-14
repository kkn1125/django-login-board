from django import template

register = template.Library()

# custom syntax
@register.filter(name="split")
def split(value, key):
    if value == None:
        return value
    else :
        return value.split(key)