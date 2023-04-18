from django import template
from django.template.loader import render_to_string
from treeMenuApp.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu():
    menu_items = MenuItem.objects.filter(parent=None).order_by('id')
    menu_html = render_to_string('menu.html', {'menu_items': menu_items})

    return menu_html
