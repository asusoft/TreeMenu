from django import template
from django.template import loader 
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
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu)
        
        return {'menu': menu, 'menu_items': menu_items}
    except Menu.DoesNotExist:
        return {'menu': '', 'menu_items': ''}
