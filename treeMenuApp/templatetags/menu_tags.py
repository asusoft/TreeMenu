from django import template
from django.urls import reverse
from treeMenuApp.models import Menu, MenuItem

register = template.Library()

def get_menu_items(menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu)
        return menu_items
    except Menu.DoesNotExist:
        return None

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):

    try:
        current_url = context['request'].path
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu)
        for item in menu_items:
            item.is_active = (current_url == item.url)
    
        return {'menu': menu, 'menu_items': menu_items, 'current_url': current_url}
    except Menu.DoesNotExist:
        return {'menu': '', 'menu_items': ''}
