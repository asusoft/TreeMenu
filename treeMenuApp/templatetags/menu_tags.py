from django import template
from django.urls import reverse
from treeMenuApp.models import Menu, MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):

    try:
        current_url = context['request'].path
        menu = Menu.objects.get(name=menu_name)
        menu_items = MenuItem.objects.filter(menu=menu)
        for item in menu_items:
            if current_url == item.url:
                item.set_is_active(True)
            else:
                item.set_is_active(False)
    
        return {'menu': menu, 'menu_items': menu_items, 'current_url': current_url}
    except Menu.DoesNotExist:
        return {'menu': '', 'menu_items': ''}
