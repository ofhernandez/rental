__author__ = 'Jose'
from django import template

register = template.Library()


@register.filter(is_safe=True)
def product(value, args):
    return value * args


@register.filter(is_safe=True)
def minus(value, args):
    return value - args