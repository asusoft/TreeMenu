from django import template
from treeMenuApp.models import MenuItem

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None).order_by('id')
    return render_template('menu.html', {'menu_items': menu_items})
