from django import template
from django.template.loader import render_to_string
from django.urls import reverse
from treeMenuApp.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_items, context):
    current_url = context.path

    for item in menu_items:
        item.is_active = (current_url == item.url)
    
    menu_html = render_to_string('menu.html', {'menu_items': menu_items})

    return menu_html
