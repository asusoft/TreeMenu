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

    result = '<ul>'
    for item in menu_items:
        if item.parent is None:
            result += f'<li><a href="{item.url}">{item.name}</a>'
            result += draw_children(item)
            result += '</li>'
    result += '</ul>'
    template = loader.get_template('menu.html')
    context = {'menu_items': result}
    return template.render(context)

def draw_children(item):
    children = item.children.all()
    if children:
        result = '<ul>'
        for child in children:
            result += f'<li><a href="{child.url}">{child.name}</a>'
            result += draw_children(child)
            result += '</li>'
        result += '</ul>'
        return result
    else:
        return ''