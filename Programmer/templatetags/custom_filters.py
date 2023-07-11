from django import template

register = template.Library()

@register.filter(name='add_css_class')
def add_css_class(field, css_class):
    attrs = field.field.widget.attrs
    attrs['class'] = attrs.get('class', '') + f' {css_class}'
    return field
