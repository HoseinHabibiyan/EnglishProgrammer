from django import template
from Programmer.custom_filters import add_css_class

register = template.Library()

register.filter('add_css_class', add_css_class)
