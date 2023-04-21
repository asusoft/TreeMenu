from django import template
from django.urls import reverse
from treeMenuApp.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
# Define a function named "draw_menu" that takes two arguments, a "context" dictionary and a "menu_name" string
def draw_menu(context, menu_name):
    try:
        current_url = context.get('request').path
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu)
        
        for item in menu_items:
            item.set_is_expanded(False)
            if current_url == item.url:
                item.set_is_active(True)
            else:
                item.set_is_active(False)
            
            if item.is_active:
                expand_item(item)

        menu_items = MenuItem.objects.filter(menu=menu)
            
        return {
            'menu': menu, 
            'menu_items': menu_items, 
            'current_url': current_url
        }
    
    except Menu.DoesNotExist:
        return {
            'menu': None, 
            'menu_items': None, 
            'current_url': None
        } 

def expand_item(item):
    """
    Recursively expands an item and its parent(s), if any.
    """
    item.set_is_expanded(True)

    if item.parent != None:
        expand_item(item.parent)