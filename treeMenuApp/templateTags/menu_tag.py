from django import template
from django.template import loader 
from django.urls import reverse

register = template.Library()

def draw_menu(menu_items, request):
    current_url = request.path

    # Find the active item and set its is_active attribute to True
    active_item = None
    for item in menu_items:
        item.is_active = (current_url == item.url)
        if item.is_active:
            active_item = item

    # Set the is_expanded attribute of each item
    for item in menu_items:
        if item.is_active:
            item.is_expanded = True
            parent = item.parent
            while parent is not None:
                parent.is_expanded = True
                parent = parent.parent
            for child in item.children:
                child.is_expanded = True
        else:
            item.is_expanded = False
            if active_item is not None and item in active_item.get_ancestors():
                item.is_expanded = True
            elif active_item is not None and active_item in item.children.all():
                item.is_expanded = True

    # Render the menu HTML
    template = loader.get_template('menu.html')
    context = {'menu_items': menu_items}
    return template.render(context, request)

