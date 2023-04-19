from django import template
from django.template import loader 
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

@register.simple_tag
def draw_menu(menu_name):
    menu_items = get_menu_items(menu_name)
    # Find the active item and set its is_active attribute to True

    # Render the menu HTML
    template = loader.get_template('menu.html')
    context = {'menu_items': menu_items}
    return template.render(context)

